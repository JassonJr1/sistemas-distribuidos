package org.acme.entity;

import io.quarkus.arc.All;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jdk.jfr.DataAmount;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.type.descriptor.sql.internal.BinaryFloatDdlType;

import java.math.BigDecimal;

@Entity
@Table(name="orderProducts")
@Data
@AllArgsConstructor
@NoArgsConstructor



public class OrderEntity {
    @Id
    @GeneratedValue

    private Long orderId;

    private Long customerId;

    private String customerName;

    private Long productId;

    private BigDecimal orderValue;

}
