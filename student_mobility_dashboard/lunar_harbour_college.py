import streamlit as st
from PIL import Image


def main():
    UNIVERSITY_NAME = "Lunar Harbor College"

    FILTERS_APPLIED = ["safety", "cost of living", "social life", "climate"]

    filter_dict = {
        "transport": "✈️",
        "safety": "🛡️",
        "cost of living": "💰",
        "ecology": "🌿",
        "social life": "🎉",
        "visa assistance": "📑",
        "climate": "☀️",
        "quality of education": "📚",
        "health and well-being": "🏥"
    }

    filter_dict_text = {
        "safety": "Lunar Harbor College takes pride in providing a safe and secure environment for its students. Located in the peaceful country of Brimstone, the college benefits from very low crime rates, ensuring that students can focus on their studies and social activities without concern. The campus is equipped with modern security measures, including 24/7 surveillance, secure dormitory access, and a dedicated campus security team. Additionally, the college fosters a community atmosphere where students look out for one another, contributing to an overall sense of safety and well-being. This commitment to security allows students at Lunar Harbor College to enjoy a worry-free and enriching academic experience.",
        "cost of living": "Lunar Harbor College offers an affordable cost of living, making it an attractive option for students from around the world. The estimated monthly cost of living is around 500 euros, which includes accommodation, food, transportation, and other essential expenses. This budget-friendly environment allows students to maintain a comfortable lifestyle without the stress of high living costs. The affordability extends to various aspects of student life, including reasonably priced dining options, cost-effective public transportation, and access to numerous free or low-cost cultural and recreational activities on campus and in the surrounding areas. By keeping living expenses manageable, Lunar Harbor College ensures that students can focus on their studies and enjoy their time abroad without financial strain.",
        "social life": "Lunar Harbor College offers a vibrant social life, ensuring students have an engaging and dynamic campus experience. With numerous clubs, organizations, and events, there's always something happening. From cultural festivals to sports tournaments, students can easily find activities that match their interests. The student union organizes regular social gatherings, fostering a lively atmosphere and helping students build lasting friendships. Located in the lively country of Brimstone, the local cafes, restaurants, and recreational facilities further enhance the social experience. Overall, Lunar Harbor College provides a rich social life, making students' time on campus enjoyable and memorable.",
        "climate": "Lunar Harbor College is nestled in the enchanting country of Brimstone, where the climate adds a delightful touch to the student experience. Summers here are pleasantly mild, with temperatures hovering around 20 degrees Celsius, perfect for enjoying the outdoors, whether it’s lounging on the campus lawns or exploring the scenic beauty of the region. As winter approaches, the temperature dips to a crisp -0.5 degrees Celsius, creating a picturesque setting that’s ideal for cozy campus gatherings and seasonal festivities. This charming climate ensures that students can embrace both the warmth of summer and the crispness of winter, making their time at Lunar Harbor College not just academically rewarding but also filled with enjoyable seasonal experiences."
    }

    st.title(UNIVERSITY_NAME)

    university_image_path = f'{UNIVERSITY_NAME.lower()}.jpg'

    # Load and resize the image
    university_image = Image.open(university_image_path)
    university_image = university_image.resize((700, 300))

    st.image(university_image, caption='')
    combined_filters = " ".join([filter_dict[filter_name]
                                for filter_name in FILTERS_APPLIED])

    # Create two columns
    col1, col2 = st.columns(2)

    # Display the combined filters string in the first column
    with col1:
        st.subheader(f"Filters: {combined_filters}")

    # Display the link button in the second column
    with col2:
        st.link_button(f"Go to {UNIVERSITY_NAME} webpage",
                       "https://openart.ai/discovery/sd-1006987203450261585", type="primary")
    st.text("")

    st.subheader("Description")
    st.write("Lunar Harbor College, located in the picturesque country of Brimstone, is a highly regarded institution, ranked 246th globally. Known for its academic excellence and supportive learning environment, the college offers a diverse range of programs in sciences, humanities, business, and arts, catering to the varied interests of its student body. The affordability of Lunar Harbor College is a significant draw, with a monthly cost of living around 500 euros, allowing students to enjoy a comfortable lifestyle without financial strain. Brimstone’s pleasant climate adds to the college’s appeal, with mild summers averaging 20 degrees Celsius and refreshing winters around -0.5 degrees Celsius, making it ideal for outdoor activities and campus events throughout the year. Lunar Harbor College is also renowned for its vibrant social life, providing numerous opportunities for students to engage in clubs, organizations, and events. The campus buzzes with activity, from cultural festivals to sports tournaments, fostering an environment where students can build lasting friendships and create unforgettable memories. Safety is a top priority, and Brimstone is known for its very low crime rates, ensuring a secure and peaceful atmosphere for students both on and off-campus. Overall, Lunar Harbor College offers a unique blend of academic rigor, affordability, pleasant climate, dynamic social life, and exceptional safety, making it an ideal destination for exchange students seeking a fulfilling and enjoyable study abroad experience.")

    # Create two columns
    col1, col2 = st.columns(2)

    # Display each category with its corresponding emoji in two columns
    categories = list(filter_dict_text.items())
    half_length = len(categories) // 2

    for category, text in categories[:half_length]:
        with col1:
            st.subheader(category.capitalize())
            st.write(f"{text}")

    for category, text in categories[half_length:]:
        with col2:
            st.subheader(category.capitalize())
            st.write(f"{text}")

    reviews = {
        "Emily Clark": {
            "rating": 5,
            "review": "The experience at Lunar Harbor College has been fantastic. The professors are supportive, and the campus life is incredibly vibrant. The climate is perfect for both studying and enjoying outdoor activities. Highly recommend!"
        },
        "Michael Johnson": {
            "rating": 5,
            "review": "Lunar Harbor College exceeded all my expectations. The affordable living costs and excellent academic programs make it a great choice. The campus is buzzing with activities, and the mild summer weather is a bonus!"
        },
        "Amanda Lee": {
            "rating": 5,
            "review": "I absolutely love studying at Lunar Harbor College. The friendly atmosphere, engaging social life, and beautiful campus make every day enjoyable. Plus, the cool winter temperatures add a unique charm to the experience."
        },
        "David Smith": {
            "rating": 4,
            "review": "Lunar Harbor College is a great place to study. The campus is lively, and there are plenty of events to attend. The cost of living is very reasonable, and the climate is quite pleasant throughout the year."
        },
        "Olivia Brown": {
            "rating": 4,
            "review": "Studying at Lunar Harbor College has been a wonderful experience. The academic programs are top-notch, and the social life is very active. The winter temperatures can be a bit chilly, but it’s all part of the charm!"
        },
        "James Wilson": {
            "rating": 3,
            "review": "Lunar Harbor College is decent. The classes are good, and the campus has a nice vibe. However, the winter weather can be a bit harsh, and some of the events are not as engaging as I had hoped."
        },
        "Sarah Davis": {
            "rating": 3,
            "review": "The college is okay overall. The cost of living is manageable, and the climate is generally pleasant. The social activities are not as frequent as I expected, but it’s still a decent place to study."
        }
    }

    # Calculate the average rating

    def calculate_average_rating(reviews):
        total_score = 0
        num_reviews = len(reviews)

        for details in reviews.values():
            total_score += details["rating"]

        average_rating = total_score / num_reviews if num_reviews > 0 else 0
        return average_rating

    # Dictionary mapping ratings to star symbols
    star_mapping = {
        5: '⭐⭐⭐⭐⭐',
        4: '⭐⭐⭐⭐☆',
        3: '⭐⭐⭐☆☆',
        2: '⭐⭐☆☆☆',
        1: '⭐☆☆☆☆',
        0: '☆☆☆☆☆'  # In case you have a 0 rating or want a default
    }

    average_rating = round(calculate_average_rating(reviews), 2)

    st.subheader("Reviews")
    # Create two columns
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader(f"Average Rating: {average_rating:.2f} {
                     star_mapping[int(average_rating)]}")

    with col2:
        selected_rating = st.selectbox("See by rating", ["all", 1, 2, 3, 4, 5])

    if selected_rating != "all":
        filtered_reviews = {name: details for name, details in reviews.items(
        ) if details["rating"] == selected_rating}
    else:
        filtered_reviews = reviews

    # Combine CSS and HTML
    css = """
    <style>
        .review-tile {
            border-radius: 10px;
            border: 1px solid white;
            padding: 20px;
            background-color: rgb(14, 17, 50);
            box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .review-tile h3 {
            margin: 0;
            color: #fff;
        }
        .review-tile p {
            color: #ccc;
        }
    </style>
    """

    html_reviews = ""

    for name, details in filtered_reviews.items():
        # Default to '☆☆☆☆☆' if rating not found
        rating = star_mapping.get(details["rating"], '☆☆☆☆☆')
        review_text = details["review"]
        html_reviews += f"""<div class="review-tile">
            <h3>{name}</h3>
            <p><strong>{rating}</strong></p>
            <p>{review_text}</p>
        </div>
        """

    # Display the combined CSS and HTML content
    st.markdown(css + html_reviews, unsafe_allow_html=True)

    if st.button('Back to Dashboard'):
        st.session_state.current_page = 'dashboard'
        st.session_state.selected_university = None
        st.experimental_rerun()


if __name__ == "__main__":
    main()
