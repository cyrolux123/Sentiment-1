import pandas as pd
import random

# Define categories and sample data
categories = ["राजनीति", "खेलकुद", "प्रविधि"]

# Sample templates for dynamic text generation
templates = {
    "राजनीति": {
        "titles": [
            "{} मा प्रधानमन्त्रीको नयाँ कदम", 
            "{} संसद् बैठक स्थगित", 
            "{} सम्बन्धमा नयाँ मस्यौदा"
        ],
        "bodies": [
            "{} को भ्रमणले आर्थिक विकासको नयाँ ढोका खोल्ने अपेक्षा गरिएको छ।",
            "{} को निर्णयले व्यापक प्रतिक्रिया ल्याएको छ।",
            "{} सम्बन्धमा सरकारको तर्फबाट चासो व्यक्त।"
        ]
    },
    "खेलकुद": {
        "titles": [
            "{} मा नेपालको ऐतिहासिक जीत", 
            "{} खेलाडीले स्वर्ण जिते", 
            "{} फाइनल खेलको तयारी"
        ],
        "bodies": [
            "{} प्रतियोगितामा नेपालको ऐतिहासिक प्रदर्शन।",
            "{} खेलाडीको मेहनतले स्वर्ण पदक नेपाललाई दिलायो।",
            "{} खेलले दर्शकको ध्यान तानेको छ।"
        ]
    },
    "प्रविधि": {
        "titles": [
            "{} प्रविधिको नयाँ प्रयोग", 
            "{} ले नयाँ उपकरण सार्वजनिक गर्‍यो", 
            "{} नेटवर्कको सुरुवात"
        ],
        "bodies": [
            "{} ले नयाँ उत्पादले बजारलाई चकित पारेको छ।",
            "{} मा एआई प्रविधिको प्रयोगले सुधार ल्याउने अपेक्षा।",
            "{} को सुरुवातले भविष्यमा गति थप्नेछ।"
        ]
    }
}

# Function to generate unique rows
def generate_data(rows):
    data = []
    for i in range(1, rows + 1):
        # Randomly choose a category
        category = random.choice(categories)
        # Generate unique title and body
        title_template = random.choice(templates[category]["titles"])
        body_template = random.choice(templates[category]["bodies"])
        keywords = ["भारत", "चीन", "एआई", "क्रिकेट", "ओलम्पिक", "फाइभजी", "नेपाल"]
        title = title_template.format(random.choice(keywords))
        body = body_template.format(random.choice(keywords))
        # Randomly determine notification priority
        notification_priority = random.choices([0, 1], weights=[0.6, 0.4])[0]
        # Append row
        data.append({
            "id": i,
            "title": title,
            "body": body,
            "notification_priority": notification_priority
        })
    return data

# Generate 500 rows
rows = 500
dataset = generate_data(rows)

# Create a DataFrame
df = pd.DataFrame(dataset)

# Save to CSV
output_file = "news_notification_dataset_nepali.csv"
df.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"Dataset with {rows} rows has been saved to {output_file}.")
