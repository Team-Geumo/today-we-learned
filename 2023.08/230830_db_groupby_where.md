## select emp_no, avg(salary) from salaries group by emp_no having avg(salary) >= 60000 order by avg(salary)

**`WHERE`**와 **`HAVING`**은 SQL에서 다른 목적으로 사용됩니다. **`WHERE`**은 그룹화하기 전의 개별 레코드들에 조건을 적용하려고 할 때 사용되며, **`HAVING`**은 **`GROUP BY`**로 그룹화된 결과에 조건을 적용하려고 할 때 사용됩니다.

주어진 쿼리에서는 **`salaries`** 테이블의 **`emp_no`** 별로 평균 급여를 구하고, 그 평균 급여가 60000 이상인 경우만 선택하라는 의미입니다. 이런 경우에는 **`GROUP BY`**가 먼저 실행되고, 그 다음에 **`HAVING`** 조건이 적용됩니다. 따라서 **`HAVING`**이 올바른 키워드입니다.

만약 **`WHERE`**을 사용한다면:

```sql
sqlCopy code
SELECT emp_no, AVG(salary)
FROM salaries
WHERE salary >= 60000
GROUP BY emp_no
ORDER BY AVG(salary);

```

이 쿼리는 각 직원의 급여가 60000 이상인 경우에만 평균을 구하라는 의미가 되어, 원하는 결과와는 다를 수 있습니다.

따라서 주어진 쿼리에서는 **`HAVING`**을 사용하는 것이 올바른 방법입니다.

https://chat.openai.com/_next/image?url=https%3A%2F%2Fs.gravatar.com%2Favatar%2Fd044cfb72b3ddc6074b872694444935e%3Fs%3D480%26r%3Dpg%26d%3Dhttps%253A%252F%252Fcdn.auth0.com%252Favatars%252Fno.png&w=96&q=75

## where avg(salary)가 안 된다는 말이야?

맞습니다. **`WHERE`** 절에서는 집계 함수를 직접 사용할 수 없습니다. **`WHERE`** 절은 결과의 집계 전, 개별 레코드에 대한 필터링을 위한 것이기 때문입니다. 집계 함수의 결과에 대한 조건을 적용하려면 **`GROUP BY`** 이후의 결과에 적용되는 **`HAVING`** 절을 사용해야 합니다.

다음과 같은 쿼리는 문법적으로 올바르지 않습니다:

```sql
sqlCopy code
SELECT emp_no, AVG(salary)
FROM salaries
WHERE AVG(salary) >= 60000
GROUP BY emp_no
ORDER BY AVG(salary);

```

**`AVG(salary)`**를 **`WHERE`** 절에서 직접 사용할 수 없습니다. 이렇게 하려면 **`HAVING`** 절을 사용해야 합니다:

```sql
sqlCopy code
SELECT emp_no, AVG(salary)
FROM salaries
GROUP BY emp_no
HAVING AVG(salary) >= 60000
ORDER BY AVG(salary);

```

결론적으로, **`WHERE`** 절에서 집계 함수를 사용하는 것은 SQL의 문법에 맞지 않습니다.