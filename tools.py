from langchain_huggingface import HuggingFaceEmbeddings
from crewai_tools import YoutubeChannelSearchTool
import os
from dotenv import load_dotenv

load_dotenv()
hf_api_key = os.getenv("HF_TOKEN")
if not hf_api_key:
    raise ValueError("HF_TOKEN missing in environment variables!")

os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_api_key

# Initialize HF embeddings
hf_embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Initialize YouTube tool with HF embeddings
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle="https://www.youtube.com/channel/UCNU_lfiiWBdtULKOw6X0Dig",
    embedding_model=hf_embeddings  # <- ensure this is passed
)
