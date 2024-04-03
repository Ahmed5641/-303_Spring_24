import wikipedia
from concurrent.futures import ThreadPoolExecutor
import time

# Part A: Sequentially Download Wikipedia Content
def download_and_save_sequentially():
    start_time = time.perf_counter()
    topics = wikipedia.search("generative artificial intelligence")
    for topic in topics:
        try:
            page = wikipedia.page(topic, auto_suggest=False)
            references = page.references
            file_name = topic.replace("/", "_") + ".txt"  # Simplified file naming
            
            with open(file_name, 'w', encoding='utf-8') as file:
                for reference in references:
                    file.write(reference + "\n")
        except Exception as e:
            print(f"An error occurred with {topic}: {e}")
    
    elapsed_time = time.perf_counter() - start_time
    print(f"Time taken for sequential download: {elapsed_time:.2f} seconds.")

# Part B: Concurrently Download Wikipedia Content
def wiki_dl_and_save(topic):
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        references = page.references
        file_name = topic.replace("/", "_") + ".txt"
        
        with open(file_name, 'w', encoding='utf-8') as file:
            for reference in references:
                file.write(reference + "\n")
    except Exception as e:
        print(f"An error occurred with {topic}: {e}")

def download_and_save_concurrently():
    start_time = time.perf_counter()
    topics = wikipedia.search("generative artificial intelligence")
    with ThreadPoolExecutor() as executor:
        executor.map(wiki_dl_and_save, topics)
    
    elapsed_time = time.perf_counter() - start_time
    print(f"Time taken for concurrent download: {elapsed_time:.2f} seconds.")

# Main section to control which part to execute
if __name__ == "__main__":
    # Uncomment the part you want to run
    
    # Run Part A
    download_and_save_sequentially()
    
    # Run Part B
    # download_and_save_concurrently()
