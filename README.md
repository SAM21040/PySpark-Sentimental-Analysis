# YouTube Comments Sentiment Analysis Dashboard

This repository contains a Streamlit-based web application for performing sentiment analysis on YouTube comments. The app fetches comments from a specified YouTube video, analyzes the sentiment of each comment using the VADER sentiment analysis tool, and provides various visualizations to display the results.

## Features

- **Data Preview**: Displays a preview of the fetched comments along with their authors, like counts, and sentiment scores.
- **Sentiment Distribution**: Shows a bar chart representing the distribution of sentiments (positive, neutral, negative) among the comments.
- **Most Liked Comments**: Lists the top 10 most liked comments with their respective sentiment scores.
- **Word Cloud**: Generates a word cloud of the most frequent words in the comments.
- **Top Words by Sentiment**: Displays bar charts of the most frequent words used in comments for each sentiment category.
- **Sentiment by Like Count**: Visualizes the distribution of like counts across different sentiment categories using a box plot.
- **Filter by Author**: Allows users to filter comments by author name.

## Installation

To run this application locally, follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/Rxghav1103/PySpark-Sentimental-Analysis.git
    cd PySpark-Sentimental-Ananlysis
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your Google API credentials:
    - In the `data.py` file in the root directory and add your YouTube Data API key under the get-dataset():
    ```python
    DEVELOPER_KEY = "YOUR_YOUTUBE_DATA_API_KEY"
    ```

5. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Enter the YouTube video ID for which you want to analyze the comments.
2. The app will fetch the comments, perform sentiment analysis, and display various visualizations to provide insights into the sentiment of the comments.

## Example

Here's an example of how the app looks:

![App Screenshot](screenshot.png)

## Dependencies

- `streamlit`
- `pandas`
- `plotly`
- `wordcloud`
- `matplotlib`
- `nltk`
- `google-api-python-client`
- `pyspark`
- `findspark`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any features, bug fixes, or enhancements.

## Acknowledgements

This project uses the following open-source libraries:
- [Streamlit](https://www.streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)
- [WordCloud](https://github.com/amueller/word_cloud)
- [Matplotlib](https://matplotlib.org/)
- [NLTK](https://www.nltk.org/)
- [Google API Python Client](https://github.com/googleapis/google-api-python-client)
- [PySpark](https://spark.apache.org/docs/latest/api/python/)

## Contact

For any questions or suggestions, feel free to contact [Raghavendra Bhargava](mailto:raghavendra.bhargava2004@gmail.com).

---

Feel free to customize this description further to fit your specific needs and preferences.
