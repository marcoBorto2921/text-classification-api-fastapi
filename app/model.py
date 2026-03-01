def predict_text(text: str):
    """
    Dummy classifier for demonstration purposes.
    Replace this with a real ML model.
    """
    if "satire" in text.lower():
        return "satirical", 0.93
    return "not_satirical", 0.87
