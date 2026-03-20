// gemini_extension.js - Main entry point for Gemini Node extension
import { app } from "/scripts/app.js";
import "./js/gemini_node.js";

app.registerExtension({
    name: "ComfyUI.Dev1_Gemini.Main",
    init() {
        console.log("Gemini Node extension initialized");
    }
}); 