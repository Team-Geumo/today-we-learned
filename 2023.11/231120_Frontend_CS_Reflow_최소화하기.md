# Reflow를 최소화하고 성능을 향상시키는 방법

## 1. Use Best-Practice Layout Techniques

-   레이아웃을 위해 인라인 스타일이나 테이블을 사용하지 않아야 합니다.

-   인라인 스타일은 HTML이 다운로드되고 추가 reflow를 트리거할 때 레이아웃에 영향을 미칩니다. 테이블은 셀 치수를 계산하기 위해 파서가 둘 이상의 패스를 필요로 하기때문에 비용이 많이 듭니다.

-   테이블 레이아웃 사용: `fixed` 는 열 너비는 헤더 행 내용을 기반으로 하므로 표 형식의 데이트를 표시할때 도움이 됩니다.

-   `flexbox` 의 위치와 크기가 HTML이 다운로드 될 때 변경될 수 있기 때문에 메인 페이지 레이아웃에 flex 아이템을 사용하면 성능이 저하 될 수 있습니다.

## 2. CSS 규칙의 수를 최소화합니다 (Minimize the Number of CSS Rules)

-   사용하는 규칙이 적을수록 reflow가 빨라집니다. 가능한 경우 복잡한 CSS Selector를 피해야 합니다.

-   이 문제는 부트스트랩과 같은 프레임워크를 사용하는 경우 특히 문제가 될 수 있습니다. 제공된 스타일중 일부를 사용하는 사이트는 거의 없습니다. 사용되지 않는 CSS, uCSS, grunt-uncss, gulp-uncss와 같은 도구는 스타일의 도구와 파일의 크기를 상당히 줄일 수 있습니다.

## 3. DOM의 깊이를 최소화합니다 (Minimize DOM depths)

-   DOM 트리의 크기와 각 branch의 요소 수를 줄여야합니다. 문서가 작고 얕을수록 reflow 될 수 있습니다. 이전 브라우저를 지원하지 않는 경우 불필요한 wrapper 요소를 제거할 수 있습니다.

## 4. 하단의 DOM 트리에서 클래스를 변경합니다 (Update Classes Low in the DOM Tree)

-   가능한 한 최대한 하단의 DOM 트리의 요소(즉, 중첩된 하위 항목이 여러 개 없는 요소)에서 클래스를 변경합니다. 이렇게 하면 reflow 범위가 필요한 만큼의 노드로 제한 될 수 있습니다. 본질적으로 중첩된 child 노드에 대한 영향이 최소인 경우에만 wrapper와 같은 부모 노드에 클래스 변경 사항을 적용합니다.

## 5. 복잡한 애니메이션 flow에서 제거합니다 (Remove Complex Animations From the Flow)

-   애니메이션이 `position: absolute;` 나 `position: fixed;` 로 문서의 flow 로 부터 제거되어 단일 요소로 적용되어 있는지 확인합니다. 이렇게 하면 문서의 다른 요소에 영향을 주지 않고 치수 및 위치를 수정할 수 있습니다.

## 6. 숨겨진 요소를 변경합니다 (Modify Hidden Elements)

-   `display: none;` 로 숨겨진 요소는 변경될 때 repaint 나 reflow 를 유발하지 않습니다. 가능한 경우 요소를 표시하기 하기전에 변경합니다.

## 7. Batch 로 요소 업데이트 (Update Elements in Batch)

-   한 번의 작업으로 모든 DOM 요소를 업데이트하여 성능을 향상시킬 수 있습니다.

## 8. 영향을 받는 요소를 제한합니다. (Limit the Affected Elements)

-   많은 수의 요소가 영향을 받을 수 있는 상황을 피하십시오. 탭을 클릭하면 다른 콘텐츠 블록이 활성화되는 캡 콘텐츠 컨트롤을 고려하세요. 각 컨텐츠 블록의 높이가 다른 경우 주변 요소에 영향을 미칩니다.
-   `container` 에 대한 고정 높이를 설정하거나 `document` 의 flow 에서 컨트롤를 제거하여 성능을 향상 시킬 수 있습니다.

## 9. 부드러운 애니메이션은 성능을 떨어뜨린다는 것을 알아야합니다. (Recognize that Smoothness Compromises Performance)

## 10 . 브라우저 툴로 repaint 이슈 분석 (Analyze Repaint Issues with Browser Tools)

-   모든 mainstream 브라우저는 reflow 가 성능에 미치는 영향을 강조하는 개발자 도구를 제공합니다. Chrome, Safari 및 Opera와 같은 Blink/Webkit 브라우저에서 TimeLine 패널을 열고 작업을 기록하세요.

## 출처

https://yoonucho.github.io/review/2019/11/22/reflow&repaint.html
