#!/usr/bin/env python
# encoding: utf-8

#Entry : https://start.spring.io/
# js: var l=[];  $('#dependencies input[type="checkbox"]').each(function(i, n ) { l.push(n.value);}); console.log('"'+ l.sort().join('", "') + '"')
CONST_LANG = ("java", "kotlin", "groovy")

CONST_PJ_TYPE = ("maven", "gradle")
CONST_DPS = ("activemq", "activiti-basic", "actuator", 
              "actuator-docs", "amqp", "aop", "artemis", 
              "azure-active-directory", 
              "azure-keyvault-secrets", "azure-storage", "azure-support", 
              "batch", "cache", "camel", "cloud-aws", "cloud-aws-jdbc", "cloud-aws-messaging", 
              "cloud-bus-amqp", "cloud-bus-kafka", "cloud-cloudfoundry-discovery", "cloud-config-client", "cloud-config-server", "cloud-connectors", 
              "cloud-contract-stub-runner", "cloud-contract-verifier", "cloud-contract-wiremock", "cloud-eureka", "cloud-eureka-server", 
              "cloud-feign", "cloud-gateway", "cloud-hystrix", "cloud-hystrix-dashboard", "cloud-oauth2", "cloud-ribbon", "cloud-security", 
              "cloud-sleuth-stream", "cloud-sleuth-zipkin-stream", "cloud-starter", "cloud-starter-consul-config", "cloud-starter-consul-discovery", 
              "cloud-starter-sleuth", "cloud-starter-vault-config", "cloud-starter-zipkin", "cloud-starter-zookeeper-config", "cloud-starter-zookeeper-discovery", 
              "cloud-stream-binder-kafka", "cloud-stream-binder-rabbit", "cloud-task", "cloud-turbine", "cloud-turbine-stream", "cloud-zuul", "configuration-processor", 
              "cxf-jaxrs", "data-cassandra", "data-cassandra-reactive", "data-couchbase", "data-couchbase-reactive", "data-elasticsearch", "data-gemfire", "data-jpa", 
              "data-ldap", "data-mongodb", "data-mongodb-reactive", "data-neo4j", "data-redis", "data-redis-reactive", "data-rest", "data-rest-hal", "data-solr", "derby", 
              "devtools", "flapdoodle-mongo", "flyway", "freemarker", "groovy-templates", "h2", "hateoas", "hornetq", "hsql", "integration", "jdbc", "jersey", "jooq", 
              "jta-atomikos", "jta-bitronix", "jta-narayana", "kafka", "keycloak", "liquibase", "lombok", "mail", "mobile", "mustache", "mybatis", "mysql", "postgresql", 
              "quartz", "ratpack", "remote-shell", "restdocs", "retry", "scs-circuit-breaker", "scs-config-client", "scs-service-registry", "security", "session", "social-facebook", 
              "social-linkedin", "social-twitter", "spring-shell", "sqlserver", "thymeleaf", "vaadin", "validation", "velocity", "web", "web-services", 
              "webflux", "websocket", "zipkin-ui")

CONST_PKG = ("jar", "war")

CONST_JVM = ("1.8", "1.7", "1.6")

CONST_DEFAULT_GROUP= "com.test"
CONST_DEFAULT_ARTIFACT= "Springboot-Example"