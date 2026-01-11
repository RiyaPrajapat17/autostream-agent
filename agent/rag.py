import json

class KnowledgeBase:
    def __init__(self, path="data/knowledge_base.json"):
        with open(path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def retrieve(self, query: str) -> str:
        q = query.lower()

        # Generic pricing questions
        if "pricing" in q or "price" in q or "plans" in q:
            return (
                "AutoStream Pricing:\n\n"
                "🔹 Basic Plan:\n"
                "- $29/month\n"
                "- 10 videos/month\n"
                "- 720p resolution\n\n"
                "🔹 Pro Plan:\n"
                "- $79/month\n"
                "- Unlimited videos\n"
                "- 4K resolution\n"
                "- AI captions\n"
            )

        # Specific plan queries
        if "basic" in q:
            return (
                "Basic Plan:\n"
                "- $29/month\n"
                "- 10 videos/month\n"
                "- 10 videos/month\n"
                "- 720p resolution"
            )

        if "pro" in q:
            return (
                "Pro Plan:\n"
                "- $79/month\n"
                "- Unlimited videos\n"
                "- 4K resolution\n"
                "- AI captions\n"
                "- 24/7 support"
            )

        # Policy queries
        if "refund" in q:
            return "No refunds are available after 7 days."

        if "support" in q:
            return "24/7 support is available only on the Pro plan."

        return "I can help with AutoStream pricing, plans, and policies."
