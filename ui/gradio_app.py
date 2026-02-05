import gradio as gr
from chains.qa_chain import answer_question

def launch_ui(vectordb):
    with gr.Blocks(title="Company Policy QA Assistant") as demo:
        gr.Markdown(
            "## Company Policy Question Answering\n"
            "Answers are generated **strictly from the documents**."
        )

        question = gr.Textbox(
            label="Ask a question",
            placeholder="What is the recruitment policy?",
            lines=2
        )

        answer = gr.Textbox(label="Answer", lines=6)

        btn = gr.Button("Get Answer")

        btn.click(
            fn=lambda q: answer_question(q, vectordb),
            inputs=question,
            outputs=answer
        )

    demo.launch()