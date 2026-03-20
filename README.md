# ComfyUI-Dev1_Gemini

A ComfyUI custom node for Google Gemini API. Supports image generation, text generation, image analysis, audio transcription, and video summarization.

## Forked From

This project is forked from [ComfyUI-IF_Gemini](https://github.com/if-ai/ComfyUI-IF_Gemini).

### Changes from Original

- **Renamed to Dev1**: All node names, class names, and categories are prefixed with `Dev1` to avoid conflicts and allow side-by-side installation with the original `IF_Gemini` package.
  - Nodes: `Dev1 Gemini`, `Dev1 Task Prompt Manager`, `Dev1 Prompt Combiner`
  - Category: `Dev1💥🎞️/Gemini`
- **model_name as free text input**: Replaced the fixed dropdown (select box) with a free-form text field, so any new model name can be used immediately without code changes.
  - Default: `gemini-3-pro-image-preview`

## Installation

1. Clone into your ComfyUI custom nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/dev1by0/ComfyUI_dev1_Gemini
```

2. Install dependencies:
```bash
cd ComfyUI_dev1_Gemini
pip install -r requirements.txt
```

3. Restart ComfyUI

## Usage

### API Key Setup

Set your Gemini API key using one of the following methods:

- **Environment variable** (recommended):
  ```bash
  # Add to ~/.zshrc or ~/.bashrc
  export GEMINI_API_KEY=your_api_key_here
  ```

- **Directly in the node**: Enter your API key in the `external_api_key` field

- **`.env` file**: Create a `.env` file in the custom node directory
  ```
  GEMINI_API_KEY=your_api_key
  ```

### Using the Node

1. Open the ComfyUI node browser and find the `Dev1💥🎞️/Gemini` category
2. Add the **Dev1 Gemini** node
3. Type the model name in `model_name` (default: `gemini-3-pro-image-preview`)
4. Set `operation_mode`:
   - `analysis` - Image/text analysis
   - `generate_text` - Text generation
   - `generate_images` - Image generation
5. Write your prompt and run

### OpenRouter Support

You can also access Gemini models through OpenRouter:

```bash
export OPENROUTER_API_KEY="sk-or-v1-your-key"
export OPENROUTER_PROXY="true"
```

Or enter your OpenRouter key in the `external_api_key` field and set `api_provider` to `openrouter`.
Type the OpenRouter model name (e.g. `google/gemini-2.5-flash-image-preview:free`) directly in the `model_name` field.

See [OPENROUTER_README.md](OPENROUTER_README.md) for details.

### Available Nodes

| Node | Description |
|------|-------------|
| **Dev1 Gemini** | Main node for text/image generation and analysis |
| **Dev1 Task Prompt Manager** | Generate prompts from predefined task presets |
| **Dev1 Prompt Combiner** | Utility node to combine multiple prompts |

## License

MIT

## Credits

- Original project: [ComfyUI-IF_Gemini](https://github.com/if-ai/ComfyUI-IF_Gemini) by [Impact Frames](https://github.com/if-ai)
