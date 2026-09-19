import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
from ree_chondrite_normalization_plotter import normalize_ree_data, calculate_anomalies

def process_ree_data(la, ce, pr, nd, sm, eu, gd, tb, dy, ho, er, tm, yb, lu):
    # Collect input values
    input_values = [la, ce, pr, nd, sm, eu, gd, tb, dy, ho, er, tm, yb, lu]
    
    # Check if any value is missing or zero
    if any(v is None or v == 0 for v in input_values):
        return gr.Plot(value=None), gr.DataFrame(value=None), gr.Markdown(value="## Error: All values must be provided and non-zero"), gr.File(value=None)
    
    # Reference values from Sun & McDonough 1989
    ref_values = [
        0.237,  # La
        0.613,  # Ce
        0.0928, # Pr
        0.457,  # Nd
        0.148,  # Sm
        0.0563, # Eu
        0.199,  # Gd
        0.0361, # Tb
        0.246,  # Dy
        0.0546, # Ho
        0.160,  # Er
        0.0247, # Tm
        0.161,  # Yb
        0.0246  # Lu
    ]
    
    # Normalize the data
    normalized_values = normalize_ree_data(input_values, ref_values)
    
    # Calculate anomalies
    ce_anomaly, eu_anomaly = calculate_anomalies(normalized_values)
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    elements = ['La', 'Ce', 'Pr', 'Nd', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu']
    ax.plot(elements, normalized_values, marker='o', linestyle='-', linewidth=2, markersize=6)
    ax.axhline(y=1, color='red', linestyle='--', label='Chondrite Reference')
    ax.set_xlabel('Rare Earth Elements')
    ax.set_ylabel('Normalized Values (log scale)')
    ax.set_title('REE Chondrite Normalization')
    ax.set_yscale('log')
    ax.grid(True, which="both", ls="--", alpha=0.5)
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Create the data table
    df = pd.DataFrame({
        'Element': elements,
        'Input (ppm)': input_values,
        'Normalized Value': normalized_values
    })
    
    # Format anomalies text
    anomalies_text = f"""
    ## Anomaly Calculations:
    - Ce/Ce* = {ce_anomaly:.3f}
    - Eu/Eu* = {eu_anomaly:.3f}
    """
    
    # Create CSV for download
    csv_content = df.to_csv(index=False)
    
    return fig, df, anomalies_text, csv_content

with gr.Blocks(title="REE Chondrite Normalization Plotter") as demo:
    gr.Markdown("# REE Chondrite Normalization Plotter")
    gr.Markdown("Enter the concentrations in ppm for each rare earth element.")
    
    with gr.Row():
        la = gr.Number(label="La (ppm)")
        ce = gr.Number(label="Ce (ppm)")
        pr = gr.Number(label="Pr (ppm)")
        nd = gr.Number(label="Nd (ppm)")
        
    with gr.Row():
        sm = gr.Number(label="Sm (ppm)")
        eu = gr.Number(label="Eu (ppm)")
        gd = gr.Number(label="Gd (ppm)")
        tb = gr.Number(label="Tb (ppm)")
        
    with gr.Row():
        dy = gr.Number(label="Dy (ppm)")
        ho = gr.Number(label="Ho (ppm)")
        er = gr.Number(label="Er (ppm)")
        tm = gr.Number(label="Tm (ppm)")
        
    with gr.Row():
        yb = gr.Number(label="Yb (ppm)")
        lu = gr.Number(label="Lu (ppm)")
    
    submit_btn = gr.Button("Submit")
    
    plot_output = gr.Plot(label="REE Normalization Plot")
    table_output = gr.DataFrame(label="Normalization Data")
    anomalies_output = gr.Markdown(label="Anomaly Calculations")
    download_btn = gr.File(label="Download CSV", interactive=False)
    
    submit_btn.click(
        fn=process_ree_data,
        inputs=[la, ce, pr, nd, sm, eu, gd, tb, dy, ho, er, tm, yb, lu],
        outputs=[plot_output, table_output, anomalies_output, download_btn]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
