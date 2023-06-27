package org.acme.controller;

import jakarta.inject.Inject;
import jakarta.transaction.Transactional;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import org.acme.dto.ProductDTO;
import org.acme.service.ProductService;

import java.beans.Transient;
import java.util.List;

@Path("/api/products")     //Tudo que for querer saber o produto,seria a parte do front-end
public class ProductController {

    @Inject
    ProductService productService;

    //Busca todos os produtos
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public List<ProductDTO> findAllProducts() {
        return productService.getAllProducts();
    }

    @GET
    @Path("/{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public ProductDTO findProductById(@PathParam("id") Long id){
        return productService.getProductById(id);
    }

    //Salva os produtos
    @POST
    @Transactional
    public Response saveProduct(ProductDTO product){
        try {
            productService.createNewProduct(product);
            return Response.ok().build();

        } catch (Exception e){
            e.printStackTrace();
            return Response.serverError().build();
        }
    }

    //Para receber alterações
    @PUT
    @Path("/{id}")
    @Transactional
    public Response changeProduct(@PathParam("id") Long id, ProductDTO product){
        try {
            productService.changeProduct(id, product);
            return Response.ok().build();

        } catch (Exception e){
            e.printStackTrace();
            return Response.serverError().build();
        }
    }


    //Delete das informações
    @DELETE
    @Path("/{id}")
    @Transactional
    public Response removeProduct(@PathParam("id") Long id){
        try {
            productService.deleteProduct(id);
            return Response.ok().build();

        } catch (Exception e){
            e.printStackTrace();
            return Response.serverError().build();
        }
    }


}




