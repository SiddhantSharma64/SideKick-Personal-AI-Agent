import gradio as gr
from sidekick import Sidekick


async def setup():
    sidekick = Sidekick()
    await sidekick.setup()
    return sidekick

async def process_message(sidekick, message, success_criteria, history):
    results = await sidekick.run_superstep(message, success_criteria, history)
    return results, sidekick
    
async def reset():
    new_sidekick = Sidekick()
    await new_sidekick.setup()
    return "", "", None, new_sidekick

def free_resources(sidekick):
    print("Cleaning up")
    try:
        if sidekick:
            sidekick.free_resources()
    except Exception as e:
        print(f"Exception during cleanup: {e}")


with gr.Blocks(title="Sidekick", theme=gr.themes.Default(primary_hue="emerald")) as ui:
    gr.Markdown("## 🤖 Sidekick Personal Assistant")
    sidekick = gr.State(delete_callback=free_resources)

    with gr.Row():
        with gr.Column():
            gr.Markdown("### 💬 Conversation")
            chatbot = gr.Chatbot(label="Assistant", height=350, type="messages")
    
    gr.Markdown("---")
    gr.Markdown("### 📝 Your Request")
    with gr.Row():
        with gr.Column(scale=4):
            message = gr.Textbox(
                show_label=True,
                label="Request",
                placeholder="Type your request to Sidekick...",
                lines=2,
                info="Describe what you want Sidekick to do."
            )
        with gr.Column(scale=3):
            success_criteria = gr.Textbox(
                show_label=True,
                label="Success Criteria",
                placeholder="What are your success criteria?",
                lines=2,
                info="How will you know if Sidekick succeeded?"
            )
        with gr.Column(scale=1, min_width=100):
            go_button = gr.Button("Go!", variant="primary", size="lg")
    
    with gr.Row():
        reset_button = gr.Button("Reset", variant="stop")
    
    ui.load(setup, [], [sidekick])
    message.submit(process_message, [sidekick, message, success_criteria, chatbot], [chatbot, sidekick])
    success_criteria.submit(process_message, [sidekick, message, success_criteria, chatbot], [chatbot, sidekick])
    go_button.click(process_message, [sidekick, message, success_criteria, chatbot], [chatbot, sidekick])
    reset_button.click(reset, [], [message, success_criteria, chatbot, sidekick])

ui.launch(inbrowser=True)