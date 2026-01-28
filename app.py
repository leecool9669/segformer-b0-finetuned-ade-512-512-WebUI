# -*- coding: utf-8 -*-
"""SegFormer B0 (ADE-512-512) 语义分割 WebUI（前端展示，不加载模型）"""
import gradio as gr

def run_segmentation(image):
    """语义分割占位：仅展示界面与结果区域，不执行模型推理。"""
    if image is None:
        return None, "请上传一张图片。\n\n加载模型后，将在此显示语义分割结果（各类别 mask 及标签，如 wall、building 等）。"
    msg = "【演示模式】未加载模型，以下为示例输出格式：\n\n"
    msg += "• 已接收图像输入\n"
    msg += "• 分割结果将包含多个类别及其二值 mask，例如：\n"
    msg += "  - wall, building, sky, tree, ...\n"
    msg += "• 加载模型后，可对每类 mask 叠加可视化并保存为图像。\n\n"
    msg += "模型基于 SegFormer-B0，在 ADE20K 上微调，输入分辨率 512×512。"
    return image, msg

with gr.Blocks(title="SegFormer B0 ADE-512-512 WebUI") as demo:
    gr.Markdown("""
    # SegFormer B0 ADE-512-512 语义分割 WebUI

    基于 SegFormer-B0、在 ADE20K 上微调的图像语义分割模型（512×512）。  
    本界面用于加载模型并进行语义分割与结果可视化。

    **模型信息**：SegFormerForSemanticSegmentation · 输入 512×512 · ADE20K 类别
    """)
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 输入")
            input_image = gr.Image(label="上传图片", type="pil", height=320)
            run_btn = gr.Button("运行分割", variant="primary", size="lg")
            clear_btn = gr.Button("清空", variant="secondary")
        with gr.Column(scale=1):
            gr.Markdown("### 输出")
            output_image = gr.Image(label="输入预览 / 分割叠加示意", type="pil", height=280)
            output_text = gr.Textbox(label="分割结果说明", lines=10, interactive=False)
    run_btn.click(fn=run_segmentation, inputs=[input_image], outputs=[output_image, output_text])

    def clear_all():
        return None, None, ""

    clear_btn.click(fn=clear_all, outputs=[input_image, output_image, output_text])

    gr.Markdown("""
    ---
    **说明**：SegFormer 采用金字塔 Transformer 编码器与轻量解码器，适用于语义分割。  
    更多相关项目源码请访问：http://www.visionstudios.ltd
    """)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, share=False)
