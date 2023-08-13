# ShapeTest.java

```
package prob6;

import java.util.ArrayList;
import java.util.List;

public class ShapeTest {

	public static void main(String[] args) {
		List<Shape> list = new ArrayList<Shape>();

		list.add( new Rectangle(5, 6) );
		list.add( new RectTriangle( 6, 2) );

		for( Shape shape : list ) {
			System.out.println( "area:" + shape.getArea() );
			System.out.println( "perimeter:" + shape.getPerimeter() );

			if( shape instanceof Resizable ) {
				Resizable resizable = (Resizable) shape;
				resizable.resize( 0.5 );
				System.out.println( "new area:" + shape.getArea() );
				System.out.println( "new perimeter:" + shape.getPerimeter() );
			}
		}
	}
}
```

# Shape.java

```
package prob6;

public abstract class Shape {
	public abstract double getArea();
	public abstract double getPerimeter();
}

```

#Resizable.java

```
package prob6;

public abstract class Shape {
	public abstract double getArea();
	public abstract double getPerimeter();
}

```

#Rectriangle.java

```
package prob6;

public class RectTriangle extends Shape {
	private double width;
	private double height;

	public RectTriangle(double width, double height) {
		this.width = width;
		this.height = height;
	}
	@Override
	public double getArea() {
		return (width * height) / 2;

	}

	@Override
	public double getPerimeter() {
		double hypotenuse = Math.sqrt(width * width + height * height);
        return width + height + hypotenuse;
	}

}

```

# Rectangle.java

```
package prob6;

public class Rectangle extends Shape implements Resizable{
	private double width;
	private double height;

	public Rectangle(double width, double height) {
		this.width = width;
		this.height = height;
	}

	@Override
	public double getArea() {
		return width * height;

	}

	@Override
	public double getPerimeter() {
		return 2*(width + height);

	}

	@Override
	public void resize(double ratio) {
		width *= ratio;
		height *= ratio;
	}

}

```
