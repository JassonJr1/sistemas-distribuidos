package org.acme.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name="customer")
@Data
@AllArgsConstructor
@NoArgsConstructor

public class CustomerEntity {

    @Id
    //identificador principal dentro do banco
    @GeneratedValue
    //vai fazer uma seguencial

    private Long id;

    private String name;

    private String phone;

    private String email;

    private String address;

    private Long age;
}
