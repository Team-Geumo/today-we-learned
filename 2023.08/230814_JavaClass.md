```
package prob3;

public class Prob2 {
	public static void main(String[] args) {
		// Duck을 Bird에서 상속받아 만들기
		Bird bird01 = new Duck();
		bird01.setName( "꽥꽥이" );
		bird01.fly();
		bird01.sing();
		System.out.println( bird01 );
		
		Bird bird02 = new Sparrow();
		bird02.setName( "짹짹" );
		bird02.fly();
		bird02.sing();
		System.out.println( bird02 );
	}
}

```


```
package prob3;

public abstract class Bird {
	protected String name;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	
	public abstract void fly();
	public abstract void sing();
}
```

```
package prob3;

public class Duck extends Bird {
	private String name;
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	@Override
	public void fly() {
		System.out.println("오리(" + getName() + ")는 날지 않습니다.");
	}

	@Override
	public void sing() {
		System.out.println("오리(" + getName() + ")가 소리내어 웁니다.");
	}
	@Override
	public String toString() {
		return "오리의 이름은 " + getName() + " 입니다.";
	}

}

```

```
package prob3;

public class Sparrow extends Bird {
	private String name;
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	@Override
	public void fly() {
		System.out.println("참새(" + getName() + ")가 날아다닙니다.");
	}

	@Override
	public void sing() {
		System.out.println("참새(" + getName() + ")가 소리내어 웁니다.");
	}
	@Override
	public String toString() {
		return "참새의 이름은 " + getName() + " 입니다.";
	}

}

```

