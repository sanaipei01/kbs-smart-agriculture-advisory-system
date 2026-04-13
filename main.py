# Smart Agriculture Advisory System

# User input
soil = input("Enter soil type (loamy/sandy/clay): ").lower()
rain = input("Enter rainfall level (low/medium/high): ").lower()
temperature = input("Enter temperature (low/medium/high): ").lower()

# Decision rules
if soil == "loamy" and rain == "low":
    crop = "Maize"
elif soil == "sandy" and rain == "high":
    crop = "Cassava"
elif soil == "clay" and rain == "medium":
    crop = "Rice"
else:
    crop = "Beans"

# Irrigation advice
if temperature == "high" and rain == "low":
    irrigation = "Irrigation needed"
else:
    irrigation = "No irrigation needed"

# Output
print("\n🌱 Recommended Crop:", crop)
print("💧 Irrigation Advice:", irrigation)
# Explanation tracking
reason = []

if soil == "loamy" and rain == "low":
    crop = "Maize"
    reason.append("Loamy soil with low rainfall is suitable for maize")

elif soil == "sandy" and rain == "high":
    crop = "Cassava"
    reason.append("Sandy soil with high rainfall supports cassava")

elif soil == "clay" and rain == "medium":
    crop = "Rice"
    reason.append("Clay soil with medium rainfall is ideal for rice")

else:
    crop = "Beans"
    reason.append("Default crop recommendation")

# Irrigation reasoning
if temperature == "high" and rain == "low":
    irrigation = "Irrigation needed"
    reason.append("High temperature and low rainfall require irrigation")
else:
    irrigation = "No irrigation needed"

# Output with explanation
print("\n🌱 Recommended Crop:", crop)
print("💧 Irrigation Advice:", irrigation)

print("\nExplanation:")
for r in reason:
    print("-", r)