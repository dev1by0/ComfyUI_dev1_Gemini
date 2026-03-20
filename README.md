# ComfyUI-Dev1_Gemini

Google Gemini API를 활용한 ComfyUI 커스텀 노드. 이미지 생성, 텍스트 생성, 이미지 분석, 오디오 트랜스크립션, 비디오 요약 등을 지원합니다.

## Fork 정보

이 프로젝트는 [ComfyUI-IF_Gemini](https://github.com/if-ai/ComfyUI-IF_Gemini)에서 포크되었습니다.

### 원본 대비 변경점

- **네이밍 변경**: 원본 프로젝트(`IF_Gemini`)와 충돌 없이 동시 설치가 가능하도록 모든 노드명, 클래스명, 카테고리를 `Dev1` 접두어로 변경
  - 노드: `Dev1 Gemini`, `Dev1 Task Prompt Manager`, `Dev1 Prompt Combiner`
  - 카테고리: `Dev1💥🎞️/Gemini`
- **model_name 텍스트 필드화**: 기존 셀렉트 박스(고정 모델 목록)를 자유 입력 텍스트 필드로 변경하여 새로운 모델명을 즉시 사용 가능
  - 기본값: `gemini-3-pro-image-preview`

## 설치

1. ComfyUI의 custom_nodes 폴더에 클론:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/dev1by0/ComfyUI_dev1_Gemini
```

2. 의존성 설치:
```bash
cd ComfyUI_dev1_Gemini
pip install -r requirements.txt
```

3. ComfyUI 재시작

## 사용법

### API 키 설정

아래 방법 중 하나로 Gemini API 키를 설정합니다:

- **환경 변수** (권장):
  ```bash
  # ~/.zshrc 또는 ~/.bashrc에 추가
  export GEMINI_API_KEY=your_api_key_here
  ```

- **노드에서 직접 입력**: `external_api_key` 필드에 API 키 입력

- **`.env` 파일**: 커스텀 노드 디렉토리에 `.env` 파일 생성
  ```
  GEMINI_API_KEY=your_api_key
  ```

### 노드 사용

1. ComfyUI 노드 브라우저에서 `Dev1💥🎞️/Gemini` 카테고리 선택
2. **Dev1 Gemini** 노드 추가
3. `model_name`에 사용할 모델명 입력 (기본값: `gemini-3-pro-image-preview`)
4. `operation_mode` 설정:
   - `analysis` - 이미지/텍스트 분석
   - `generate_text` - 텍스트 생성
   - `generate_images` - 이미지 생성
5. 프롬프트 작성 후 실행

### OpenRouter 사용

OpenRouter를 통해 Gemini 모델에 접근할 수도 있습니다:

```bash
export OPENROUTER_API_KEY="sk-or-v1-your-key"
export OPENROUTER_PROXY="true"
```

또는 노드의 `external_api_key`에 OpenRouter 키를 입력하고 `api_provider`를 `openrouter`로 설정합니다.
모델명은 OpenRouter 형식(예: `google/gemini-2.5-flash-image-preview:free`)을 `model_name` 필드에 직접 입력합니다.

자세한 내용은 [OPENROUTER_README.md](OPENROUTER_README.md)를 참고하세요.

### 제공 노드

| 노드 | 설명 |
|------|------|
| **Dev1 Gemini** | 메인 노드. 텍스트/이미지 생성, 분석 등 수행 |
| **Dev1 Task Prompt Manager** | 미리 정의된 태스크 프리셋으로 프롬프트 생성 |
| **Dev1 Prompt Combiner** | 여러 프롬프트를 결합하는 유틸리티 노드 |

## License

MIT

## Credits

- 원본 프로젝트: [ComfyUI-IF_Gemini](https://github.com/if-ai/ComfyUI-IF_Gemini) by [Impact Frames](https://github.com/if-ai)
