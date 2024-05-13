import jinja2
import seaborn as sns
import pandas as pd


def color_negative_red(val):
    color = 'red' if val else 'black'
    return f'color: {color}'


def generate_html_report(df, runs_number):
    # Styling
    styler = df.style.applymap(color_negative_red)

    df.to_csv('data.csv', index=False)

    # Aggregation
    average_time_per_target = df.groupby(['Target', 'Algorithm']).agg({'Time': 'mean', 'Degree Centrality': 'first'}).reset_index()
    average_time_per_target.sort_values(by=["Target"], inplace=True)
    algorithm_list = average_time_per_target["Algorithm"].unique().tolist()

    # Find algorithm with maximum time
    max_time_index = average_time_per_target["Time"].idxmax()
    algorithm_max_time = average_time_per_target.loc[max_time_index, "Algorithm"]

    # Find algorithm with minimum time
    min_time_index = average_time_per_target["Time"].idxmin()
    algorithm_min_time = average_time_per_target.loc[min_time_index, "Algorithm"]

    # Template handling
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=''))
    template = env.get_template('./task_utils/template.html')
    html_content = template.render(my_table=average_time_per_target.to_html(index=False),
                                   algorithms=algorithm_list,
                                   runs_number=runs_number,
                                   best_algorithm=algorithm_min_time,
                                   worst_algorithm=algorithm_max_time,
                                   )

    # Plot
    plot = sns.relplot(x="Degree Centrality", y="Time", hue="Algorithm", kind="scatter", data=average_time_per_target)
    plot.savefig('plot.svg')
    return html_content


def save_html_report(html_content, filename='report.html'):
    with open(filename, 'w') as f:
        f.write(html_content)
    print(f"HTML report saved as '{filename}'")


def open_html_report_in_browser(filename='report.html'):
    import webbrowser
    webbrowser.open_new_tab(filename)
