package org.acme.service;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import jakarta.ws.rs.NotFoundException;
import org.acme.client.CustomerClient;
import org.acme.client.ProductClient;
import org.acme.dto.CustomerDTO;
import org.acme.dto.OrderDTO;
import org.acme.dto.ProductDTO;
import org.acme.entity.OrderEntity;
import org.acme.repository.OrderRepository;
import org.eclipse.microprofile.rest.client.inject.RestClient;

import java.util.ArrayList;
import java.util.List;

@ApplicationScoped
public class OrderService {
    @Inject
    private OrderRepository orderRepository;

    @Inject
    @RestClient
    private CustomerClient customerClient;

    @Inject
    @RestClient
    private ProductClient productClient;

    public List<OrderDTO> getAllOrders(){

        List<OrderDTO> orders = new ArrayList<>();

        orderRepository.findAll().stream().forEach(item->{
            orders.add(mapEntityToDTO(item));
        });

        return orders;

    }

    public void saveNewOrder(OrderDTO orderDTO){

        CustomerDTO customerDTO = customerClient.getCustomerById(orderDTO.getCustomerId());

        if (customerDTO.getName().equals(orderDTO.getCustomerName())
                && productClient.getProductById(orderDTO.getProductId()) != null){
            orderRepository.persist(mapDTOToEntity(orderDTO));
        } else {
            throw new NotFoundException();
        }
    }

    private OrderDTO mapEntityToDTO(OrderEntity item){

        OrderDTO orderDTO = new OrderDTO();

        orderDTO.setCustomerId(item.getCustomerId());
        orderDTO.setOrderValue(item.getOrderValue());
        orderDTO.setCustomerName(item.getCustomerName());
        orderDTO.setProductId(item.getProductId());

        return orderDTO;
    }

    private OrderEntity mapDTOToEntity(OrderDTO item){

        OrderEntity orderEntity = new OrderEntity();

        orderEntity.setCustomerId(item.getCustomerId());
        orderEntity.setOrderValue(item.getOrderValue());
        orderEntity.setCustomerName(item.getCustomerName());
        orderEntity.setProductId(item.getProductId());

        return orderEntity;
    }

}
