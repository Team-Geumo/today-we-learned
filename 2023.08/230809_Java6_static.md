```
package prob02;

import java.util.Scanner;

public class GoodsApp {
	static class Goods{
		String beverage;
		int price;
		int stock;

		public Goods(String beverage, int price, int stock){
			this.beverage = beverage;
			this.price = price;
			this.stock = stock;
		}
	}
	private static final int COUNT_GOODS = 3;

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		Goods[] goods = new Goods[COUNT_GOODS];

		// 상품 입력
		for (int i = 0; i < COUNT_GOODS; i++){
			String line = scanner.nextLine();
			String infos[] = line.split(" ");
			String beverage = infos[0];
			int price = Integer.parseInt(infos[1]);
			int stock = Integer.parseInt(infos[2]);
//			goods[i] = new Goods(beverage, price, stock);
		}
		// 상품 출
		
		// 자원정리
		scanner.close();
	}

}

//static 키워드를 사용하는 이유는 Goods 클래스가 GoodsApp 클래스의 내부에 정의되어 있기 때문입니다. 내부 클래스가 static이 아닌 경우, 외부 클래스의 인스턴스와 연결되어 있어야 하며, 외부 클래스의 인스턴스 없이 내부 클래스의 인스턴스를 생성할 수 없습니다.
//
//static 내부 클래스는 이러한 연결이 필요하지 않습니다. static 키워드가 붙은 내부 클래스는 외부 클래스의 인스턴스와 독립적이며, 외부 클래스의 인스턴스 없이도 직접 인스턴스화 할 수 있습니다.
//
//이 경우 Goods 클래스는 GoodsApp 클래스의 main 메서드에서 독립적으로 사용되어야 하므로, Goods 클래스를 static으로 선언해야 합니다. 이렇게 하면 GoodsApp 클래스의 인스턴스 없이도 Goods 객체를 생성할 수 있게 되어, 코드에서 빨간 줄이 사라집니다.
//
//물론, Goods 클래스를 완전히 독립된 외부 클래스로 정의하는 것도 가능한 해결책입니다. 이렇게 하면 GoodsApp 클래스 내부에서도 Goods 객체를 자유롭게 생성할 수 있습니다.
```