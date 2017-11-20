package org.test

import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.SpringBootApplication

@SpringBootApplication
class TestSpringbootApplication

fun main(args: Array<String>) {
    SpringApplication.run(TestSpringbootApplication::class.java, *args)
}
