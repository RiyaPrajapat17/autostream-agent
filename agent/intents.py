def detect_intent(message: str) -> str:
    """
    Explicit, rule-based intent detection.
    This is deterministic, explainable, and production-safe.
    """

    msg = message.lower().strip()

    # 1️⃣ Casual Greeting
    if any(word in msg for word in [
        "hi", "hello", "hey", "hii", "good morning", "good evening"
    ]):
        return "CASUAL_GREETING"

    # 2️⃣ High-Intent Lead (Ready to sign up)
    if any(phrase in msg for phrase in [
        "sign up",
        "get started",
        "subscribe",
        "i want",
        "i would like",
        "try",
        "start using",
        "join",
        "buy",
        "purchase"
    ]):
        return "HIGH_INTENT_LEAD"

    # 3️⃣ Product / Pricing / Policy Inquiry
    if any(keyword in msg for keyword in [
        "price",
        "pricing",
        "cost",
        "plan",
        "plans",
        "feature",
        "features",
        "basic",
        "pro",
        "refund",
        "refund policy",
        "support",
        "policy",
        "help"
    ]):
        return "PRODUCT_INQUIRY"

    # 4️⃣ Fallback
    return "UNKNOWN"
