# 이중등호(==), 삼중등호(===), Object.is()

## 이중등호(동등 비교 연산자, loose equality operator)

피연산자를 비교할 때 먼저 **암묵적 타입 변환**을 통해 타입을 일치시킨 후 비교함<br>
결과를 예측하기 어렵고 실수하기 쉬우므로 일치 비교 연산자를 권장함<br>

## 삼중등호(일치 비교 연산자, strict equality operator)

피연산자의 **타입과 값이 모두 같을 경우에만** true를 반환함<br>
암묵적 타입 변환을 하지 않기 때문에 예측하기 쉬움<br>

-   동등 비교 연산자, 일치 비교 연산자 모두 **양의 0**과 **음의 0**을 같다고 판단함

    ```js
    0 == -0; // true
    0 === -0; // true
    ```

-   **주의 사항** : `NaN`은 자신과 일치하지 않는 유일한 값으로, 숫자가 `NaN`인지 조사하려면 `Number.isNaN`을 사용해야 함

    ```js
    NaN === NaN; // false

    Number.isNaN(NaN); // true
    Number.isNaN(10); // false
    Number.isNaN(1 + undefined); // true
    ```

## Object.is()

예측 가능한 정확한 비교 결과를 반환하는 메서드<br>

```js
-0 === 0; // true
Object.is(-0, +0); // false

NaN === NaN; // false
Object.is(NaN, NaN); // true
```

<table>
<tr align=center>
<td><b>value1</b></td>
<td><b>value2</b></td>
<td><b>==</b></td>
<td><b>===</b></td>
<td><b>Object.is</b></td>
</tr>
<tr align=center>
<td>undefined</td>
<td>undefined</td>
<td>true</td>
<td>true</td>
<td>true</td>
</tr>
<tr align=center>
<td>null</td>
<td>null</td>
<td>true</td>
<td>true</td>
<td>true</td>
</tr>
<tr align=center>
<td>true</td>
<td>true</td>
<td>true</td>
<td>true</td>
<td>true</td>
</tr>
<tr align=center>
<td>false</td>
<td>false</td>
<td>true</td>
<td>true</td>
<td>true</td>
</tr>
<tr align=center>
<td>'foo'</td>
<td>'foo'</td>
<td>true</td>
<td>true</td>
<td>true</td>
</tr>
<tr align=center>
<td>0</td>
<td>0</td>
<td>true</td>
<td>true</td>
<td>true</td>
</tr>
<tr align=center>
<td>+0</td>
<td>-0</td>
<td>true</td>
<td>true</td>
<td>false</td>
</tr>
<tr align=center>
<td>+0</td>
<td>0</td>
<td>true</td>
<td>true</td>
<td>true</td>
</tr>
<tr align=center>
<td>-0</td>
<td>0</td>
<td>true</td>
<td>true</td>
<td>false</td>
</tr>
<tr align=center>
<td>0n</td>
<td>-0n</td>
<td>true</td>
<td>true</td>
<td>true</td>
</tr>
<tr align=center>
<td>0</td>
<td>false</td>
<td>true</td>
<td>false</td>
<td>false</td>
</tr>
<tr align=center>
<td>""</td>
<td>false</td>
<td>true</td>
<td>false</td>
<td>false</td>
</tr>
<tr align=center>
<td>""</td>
<td>0</td>
<td>true</td>
<td>false</td>
<td>false</td>
</tr>
<tr align=center>
<td>'0'</td>
<td>0</td>
<td>true</td>
<td>false</td>
<td>false</td>
</tr>
<tr align=center>
<td>'17'</td>
<td>17</td>
<td>true</td>
<td>false</td>
<td>false</td>
</tr>
<tr align=center>
<td>[1, 2]</td>
<td>'1,2'</td>
<td>true</td>
<td>false</td>
<td>false</td>
</tr>
<tr align=center>
<td>new String('foo')</td>
<td>'foo'</td>
<td>true</td>
<td>false</td>
<td>false</td>
</tr>
<tr align=center>
<td>null</td>
<td>undefined</td>
<td>true</td>
<td>false</td>
<td>false</td>
</tr>
<tr align=center>
<td>null</td>
<td>false</td>
<td>false</td>
<td>false</td>
<td>false</td>
</tr>
<tr align=center>
<td>undefined</td>
<td>false</td>
<td>false</td>
<td>false</td>
<td>false</td>
</tr>
<tr align=center>
<td>{ foo: 'bar' }</td>
<td>{ foo: 'bar' }</td>
<td>false</td>
<td>false</td>
<td>false</td>
</tr>
<tr align=center>
<td>new String('foo')</td>
<td>new String('foo')</td>
<td>false</td>
<td>false</td>
<td>false</td>
</tr>
<tr align=center>
<td>0</td>
<td>null</td>
<td>false</td>
<td>false</td>
<td>false</td>
</tr>
<tr align=center>
<td>0</td>
<td>NaN</td>
<td>false</td>
<td>false</td>
<td>false</td>
</tr>
<tr align=center>
<td>'foo'</td>
<td>NaN</td>
<td>false</td>
<td>false</td>
<td>false</td>
</tr>
<tr align=center>
<td>NaN</td>
<td>NaN</td>
<td>false</td>
<td>false</td>
<td>true</td>
</tr>
</table>

## isEqual()

자바스크립트에서 객체들은 값으로 비교되는 것이 아니라 **참조로 비교됨**<br>
lodash는 객체를 값으로 비교하는 메서드 `isEqual()`을 제공함

```js
import _ from 'lodash';

const stringObj1 = new String('foo');
const stringObj2 = new String('foo');

stringObj1 == stringObj2; // false
stringObj1 === stringObj2; // false
Object.is(stringObj1, stringObj2); // false
_.isEqual(stringObj1, stringObj2); // true
```
