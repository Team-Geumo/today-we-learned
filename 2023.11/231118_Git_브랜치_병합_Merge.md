# Git의 브랜치 병합 방법 (Merge)

## 1. Merge

-   일반적으로 사용되는 병합 방법
-   commit 이력이 모두 그대로 남아있음
-   **Fast-Forward** 방식과 **Recursive** 방식으로 나뉨

```bash
git checkout main
git merge my-branch
```

### Fast-Forward

-   새로운 브랜치 (`my-branch`)가 `main` 브랜치로부터 분기된 이후 `main` 브랜치에 새로운 Commit이 올라오지 않았을 때
-   my-branch가 main과 비교하여 최신의 브랜치이므로 `my-branch`의 변경 이력을 그대로 `main`으로 가져올 수 있음

### Recursive

-   my-branch가 main 브랜치에서 분기된 이후 `main` 브랜치에 새로운 Commit이 생겼을 때
-   my-branch가 최신의 브랜치가 아니므로 `my-branch`와 `main`을 공통 부모로 한 새로운 Merge Commit을 생성함
-   Fast-Forward Merge가 가능한 상태에서 `--no-ff` 옵션을 주면 강제로 Merge Commit을 생성할 수 있음

```bash
git merge my-branch --no-ff
```

## 2. Squash & Merge

-   병합할 브랜치의 모든 Commit을 하나의 Commit으로 Squash한 새로운 Commit을 `main` 브랜치에 추가함
-   **주의** : Squash 후에는 모든 Commit 이력이 하나로 합쳐지면서 기존 Commit 내역들이 사라짐

```bash
git checkout main
git merge my-branch --squash
git commit -m "Squash & Merge"
```

## 3. Rebase & Merge

-   Base : my-branch가 분기된 시점의 `main` 브랜치 Commit
-   Base를 main 브랜치의 최신 Commit으로 재설정(**Rebase**)한 후 `main` 브랜치에 추가
-   **주의** : Rebase 시 Commit Hash가 변경되어 Force Push를 해야 할 경우가 생길 수 있음

```bash
git checkout my-branch
git rebase main
git checkout main
git merge my-branch
```

## 4. 사용 예시

### 1. `develop` - `feature` 브랜치 간 머지 : Squash and Merge

-   `feature`의 Commit History를 모두 묶어 새로운 Commit으로 `develop` 브랜치에 추가해 `develop` 브랜치에서 독자적으로 관리할 수 있음
-   일반적으로 Merge 후에 `feature` 브랜치를 삭제해버리는 점을 떠올려 보면, `feature` 브랜치의 Commit History를 모두 `develop` 브랜치에 직접 연관 지어 남길 필요가 없음

### 2. `main` - `develop` 브랜치 간 머지 : Rebase and Merge

-   `develop`의 내용을 `main`에 추가할 때에는 별도의 새로운 Commit을 생성할 이유가 없기 때문

### 3. `hotfix` - `develop`, `hotfix` - main 브랜치 간 머지 : Merge 또는 Squash and Merge

-   `hotfix` 브랜치 작업의 각 Commit History가 모두 남아야 하는 경우 Merge
-   `hotfix` 브랜치 작업의 각 Commit History가 필요 없는 경우 Squash and Merge

## 출처

https://meetup.nhncloud.com/posts/122
https://hudi.blog/git-merge-squash-rebase/
