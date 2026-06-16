import os
import streamlit as st
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI

# =========================================================================
# 🔑 আপনার ফ্রি Gemini API Key সরাসরি এখানে বসানো হয়েছে
# =========================================================================
os.environ["GEMINI_API_KEY"] = "AQ.Ab8RN6IE8IlgxGnwq-78dVH3J7t3pcR0Tj1GEgzGIUnH3q6PIQ"

# Streamlit ওয়েব接口 ডিজাইন
st.set_page_config(page_title="AI Agent Hub", layout="centered", page_icon="🤖")
st.title("🤖 Free AI Agent: ডেটা অ্যানালিসিস ও কনটেন্ট রাইটার")
st.write("আপনার যেকোনো ডেটা বা টেক্সট ইনপুট দিন, এআই এজেন্ট সেটি নিখুঁতভাবে বিশ্লেষণ করে চমৎকার বাংলা কন্টেন্ট তৈরি করে দেবে।")

# ইউজার থেকে ইনপুট নেওয়ার টেক্সট বক্স
user_data = st.text_area(
    "বিশ্লেষণ করার জন্য আপনার ডেটা বা টপিকটি এখানে লিখুন:", 
    height=150, 
    placeholder="যেমন: ২০২৬ সালে বাংলাদেশে টেকনোলজি এবং এআই রিলেটেড কনটেন্টের ভিউয়ারশিপ ৪৫% বৃদ্ধি পেয়েছে..."
)

# এজেন্ট রান করার বাটন
if st.button("এজেন্ট রান করুন 🚀"):
    if not user_data:
        st.warning("⚠️ দয়া করে বিশ্লেষণ করার জন্য কিছু ডেটা বা টেক্সট ইনপুট দিন।")
    elif os.environ["GEMINI_API_KEY"] == "এখানে_আপনার_গুগল_এআই_স্টুডিওর_ফ্রি_কী_বসাবেন":
        st.error("❌ Error: দয়া করে কোডের শুরুর দিকে আপনার আসল GEMINI_API_KEY টি বসান।")
    else:
        # লোডিং অ্যানিমেশন চালু
        with st.spinner("এআই এজেন্টরা কাজ করছে... দয়া করে একটু অপেক্ষা করুন..."):
            try:
                # সম্পূর্ণ ফ্রিতে গুগলের Gemini 1.5 Flash মডেল সেটআপ
                llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", verbose=True)

                # ১. ডেটা অ্যানালিস্ট এজেন্ট তৈরি
                data_analyst = Agent(
                    role='Senior Data Analyst',
                    role_description='প্রদত্ত ডেটা নিখুঁতভাবে বিশ্লেষণ করে গুরুত্বপূর্ণ ইনসাইট এবং ট্রেন্ড খুঁজে বের করা।',
                    goal='ডেটার গভীরে গিয়ে মূল প্যাটার্ন ও সামারি বের করা।',
                    backstory='আপনি একজন অভিজ্ঞ ডেটা বিজ্ঞানী। যেকোনো জটিল তথ্য থেকে আসল সত্য ও ট্রেন্ড খুঁজে বের করাই আপনার কাজ।',
                    verbose=True,
                    llm=llm
                )

                # ২. কনটেন্ট রাইটার এজেন্ট তৈরি
                content_writer = Agent(
                    role='Professional Content Writer & SEO Specialist',
                    role_description='অ্যানালিস্টের দেওয়া ডেটার ওপর ভিত্তি করে তথ্যবহুল ও আকর্ষণীয় বাংলা আর্টিকেল বা স্ক্রিপ্ট তৈরি করা।',
                    goal='জরিপ বা তথ্যের জটিল অংশগুলোকে সাধারণ মানুষের উপযোগী করে আকর্ষণীয় ও সাবলীল বাংলায় রূপান্তর করা।',
                    backstory='আপনি একজন দক্ষ ডিজিটাল কন্টেন্ট ক্রিয়েটর।专অ্যানালিস্টের দেওয়া বোরিং ডেটাকে আপনি চমৎকার ও ভাইরাল সোশ্যাল মিডিয়া কন্টেন্টে রূপান্তর করতে পারেন।',
                    verbose=True,
                    llm=llm
                )

                # টাস্ক বা কাজের বিবরণ সেটআপ
                task1 = Task(
                    description=f'নিচের ডেটাটি বিশ্লেষণ করুন এবং প্রধান ৩টি ট্রেন্ড বা ইনসাইট বের করুন:\n{user_data}',
                    expected_output='পয়েন্ট আকারে মূল ইনসাইট এবং ট্রেন্ডের একটি সংক্ষিপ্ত তালিকা।',
                    agent=data_analyst
                )

                task2 = Task(
                    description='অ্যানালিস্টের দেওয়া রিপোর্টের ওপর ভিত্তি করে ফেসবুক, ইউটিউব বা ব্লগের জন্য একটি আকর্ষণীয় বাংলা কন্টেন্ট/স্ক্রিপ্ট লিখুন। কন্টেন্টে অবশ্যই একটি সুন্দর শিরোনাম এবং আকর্ষণীয় হুক থাকতে হবে।',
                    expected_output='আকর্ষণীয় শিরোনামসহ পয়েন্ট আকারে সাজানো একটি সম্পূর্ণ বাংলা কন্টেন্ট।',
                    agent=content_writer
                )

                # ক্রু (Crew) গঠন ও রান করা
                analysis_crew = Crew(
                    agents=[data_analyst, content_writer],
                    tasks=[task1, task2],
                    process=Process.sequential
                )
                
                # এজেন্টদের কাজ শুরু করা
                result = analysis_crew.kickoff()
                
                # ওয়েবসাইটে ফলাফল প্রদর্শন
                st.success("✅ এজেন্টরা সফলভাবে কাজ শেষ করেছে!")
                st.markdown("---")
                st.subheader("📝 এআই এজেন্টের তৈরি করা কন্টেন্ট:")
                st.markdown(result)
                
            except Exception as e:
                st.error(f"একটি সমস্যা হয়েছে: {e}")
