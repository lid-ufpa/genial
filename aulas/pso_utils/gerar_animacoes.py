from IPython.display import HTML


def gerar_animacao(animacao):
    videos_html = "".join(
        f'<div style="margin: 10px;">{animacao[i].to_html5_video()}</div>' for i in range(3)
    )

    return HTML(f"""
    <div style="display: flex; justify-content: center; align-items: flex-start;">
        {videos_html}
    </div>
    """)
