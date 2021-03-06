Regular Expression HOWTO

작성자  
A.M. 쿠클링 <amk@amk.ca>  

요약  
이 문서는 Python에서 정규식을 re 모듈에서 사용하기 위한 입문 자습서입니다. Library Reference의 해당 섹션보다 더 부드러운 소개를 제공합니다.

서론  

정규식(RE, regex, regex 또는 regex 패턴이라고 함)은 기본적으로 파이썬 내부에 내장되어 있고 re 모듈을 통해 사용할 수 있는 매우 작은 전문 프로그래밍 언어입니다. 
이 작은 언어를 사용하여 일치시킬 수 있는 문자열 집합에 대한 규칙을 지정합니다. 
이 집합에는 영어 문장, 전자 메일 주소, TeX 명령 또는 원하는 항목이 포함될 수 있습니다. 그런 다음 <이 끈이 패턴과 일치합니까?> 또는 <이 끈 어디에도 패턴과 일치하는 것이 있습니까?>와 같은 질문을 던질 수 있다. 또한 RE를 사용하여 문자열을 수정하거나 다양한 방법으로 분할할 수 있습니다.

정규식 패턴은 일련의 바이트 코드로 컴파일되며, 이 바이트 코드는 C로 작성된 일치하는 엔진에 의해 실행됩니다. 고급 사용을 위해 엔진이 지정된 RE를 실행하는 방법에 주의하여 RE를 작성해야 더 빨리 실행되는 바이트 코드를 만들 수 있습니다. 최적화는 이 문서에서는 다루지 않습니다. 이 문서에서는 일치하는 엔진의 내부를 잘 이해해야 하기 때문입니다.

정규식 언어는 상대적으로 작고 제한적이기 때문에 가능한 모든 문자열 처리 작업을 정규식을 사용하여 수행할 수 없습니다. 정규 표현으로 할 수 있는 업무도 있지만, 표현은 매우 복잡한 것으로 밝혀졌습니다. 이러한 경우 처리를 위해 Python 코드를 쓰는 것이 더 나을 수 있습니다. Python 코드는 정교한 정규식보다 느리지만, 더 이해할 수 있을 것입니다.
