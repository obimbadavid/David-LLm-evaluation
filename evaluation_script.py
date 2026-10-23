def evaluate_llm_model(model, dataset,output_path='results.json):
    doc = Document('David.docx')
    text ='\n'.join([p.text for p in doc.paragraphs])
    return text
