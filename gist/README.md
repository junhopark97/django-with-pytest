## pytest 파일 설정
### pytest에서 test를 하기 위해 파일 앞에 test 접두사를 사용하여 파일을 호출하게 만든다.

```
test 명령어
1. pytest {경로} -v  (해당 경로만 테스트)
2. test .  (전체 테스트)
```

## @pytest.mark.skip 
```
건너뛰고 싶은 테스트에 적용을 한다.
ex) 버그가 발생하여 실패한 테스트인 경우,
    테스트를 지우고 데이터와 테스트를 작성하기 위해 투입한 모든 작업을 잃고 싶지 않을 때.

* 버그를 수정될 때까지 이 테스트를 실행하지 않고 테스트를 하기 위함.
```

## @pytest.mark.skipif()
```
조건에 맞게 skip하고 싶을 때 사용.
```

## @pytest.mark.xfail
```
테스트가 fail할 것임을 가르키며, 테스트 실행에 문제 없이 패스하게 된다.
테스트에 성공을 하게 되면 XPASS의 결과를 리턴한다.
```

## @pytest.mark.slow
```
단독 테스트를 하고 싶을 때 사용한다.
slow 마크는 가장 타이트하게 등록해야 되기 때문에 경고를 받게 된다.

테스트 명령어
1. pytest {경로} -v -p no:warnings  (경고를 숨기고 억제)
2. pytest {경로} -v -p no:warnings -m slow  (slow 표시가 있는 슬로프에 태그가 지정된 테스트만 실행)
3. pytest {경로} -v -p no:warnings -m 'not slow'  (slow 제외하고 테스트 실행)
```

## @pytest.fixture
```
테스트 할때 db, object 등 필요한 데이터를 미리 세팅하여 사용할 수 있도록 하는 데코레이터이다.

테스트 명령어
: pytest {path} -v -p no:warnings -s
```

## @pytest.mark.parametrize
```
테스트 함수의 매개변수로 매개변수가 들어갔을 때의 값을 예상하는 테스트이다.
ids(62번 줄)는 매개변수화된 테스트로 레이블을 지정한 ID이다.
```
gist/test_gist.py::test_parametrized <span style='color: red'>[TIKTOK TEST]</span> <br /> 
Test with TikTok <br /> 
<span style='color: #008000'> PASSED </span> <br /> 
gist/test_gist.py::test_parametrized <span style='color: red'>[INSTAGRAM TEST] </span> <br /> 
Test with Instagram <br /> 
<span style='color: #008000'> PASSED </span> <br /> 
gist/test_gist.py::test_parametrized <span style='color: red'>[TWITCH TEST] </span> <br />
Test with Twitch <br /> 
<span style='color: #008000'> PASSED </span> <br /> 

