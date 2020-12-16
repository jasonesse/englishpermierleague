from loader import data_loader

def run():
    source_df = data_loader.source_load(debug=True)

if __name__ == '__main__':
    run()