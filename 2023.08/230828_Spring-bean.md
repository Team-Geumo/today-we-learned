```
package spring.learningspringframework;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class App02HelloWorldSpring {

	public static void main(String[] args) {
		// 1: Launch a Spring Context
		var context = new AnnotationConfigApplicationContext(HelloWorldConfiguration.class);
		// 2: Configure the things that we want Spring to manage - @Configuration

		// 3: 스프링이 관리하는 Bean을 검색
		System.out.println(context.getBean("name"));
		System.out.println(context.getBean("age"));
		System.out.println(context.getBean("person"));
		System.out.println(context.getBean("person2"));
		System.out.println(context.getBean("person3"));
		System.out.println(context.getBean("address"));
		System.out.println(context.getBean(Address.class));
	}

}
```

```
package spring.learningspringframework;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

// jdk 16
// setter getter method를 만들 필요가 없어짐
record Person(String name, int age, Address address) {
};

record Address(String firstLineString, String city) {
};

@Configuration
public class HelloWorldConfiguration {

	@Bean
	public String name() {
		return "dawn";
	}

	@Bean
	public int age() {
		return 29;
	}

	@Bean
	public Person person() {
		return new Person("dawn", 29, new Address("songlidan", "Seoul"));
	}

	@Bean
	public Person person2() {
		return new Person(name(), age(), address());
	}

	@Bean
	public Person person3(String name, int age, Address address) {
		return new Person(name(), age(), address());
	}

	@Bean
	public Address address() {
		return new Address("bakjae", "Seoul");
	}

	// 안 됨
//	@Bean
//	public Address Hi() {
//		return new Address("roro", "piana");
//	}
}

```
