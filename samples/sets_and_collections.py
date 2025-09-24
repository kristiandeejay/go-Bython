class DataProcessor {
    def __init__(self, initial_tags=set(), config={}) {
        self.tags = initial_tags;
        self.config = config;
        self.results = {};
    }

    def add_tags(self, *tags) {
        for tag in tags {
            self.tags.add(tag);
        }
    }

    def process_numbers(self, numbers) {
        squares = {x*x for x in numbers};
        evens = {n for n in numbers if n % 2 == 0};

        return {
            "squares": squares,
            "evens": evens,
            "count": len(numbers)
        };
    }

    def create_mapping(self, items) {
        id_map = {item["id"]: item["name"] for item in items};
        return id_map;
    }
}

def analyze_data(data_set, filters={}) {
    unique_values = {
        item["value"]
        for item in data_set
        if item.get("active", True)
    };

    grouped = {
        "values": unique_values,
        "total": len(unique_values),
        "metadata": {
            "processed": True,
            "filters": filters
        }
    };

    return grouped;
}

def merge_collections(set1, set2, dict1={}, dict2={}) {
    combined_set = set1 | set2;
    combined_dict = {**dict1, **dict2};

    return combined_set, combined_dict;
}

if __name__ == "__main__" {
    processor = DataProcessor(
        initial_tags={"python", "golang", "rust"},
        config={"mode": "fast", "verbose": True}
    );

    print("Initial tags:", processor.tags);

    processor.add_tags("java", "c++");
    print("After adding tags:", processor.tags);

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    result = processor.process_numbers(numbers);
    print("\nNumber processing result:");
    print(f"  Squares: {result['squares']}");
    print(f"  Evens: {result['evens']}");
    print(f"  Count: {result['count']}");

    items = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ];

    mapping = processor.create_mapping(items);
    print("\nID Mapping:", mapping);

    data_set = [
        {"value": "a", "active": True},
        {"value": "b", "active": False},
        {"value": "c", "active": True},
        {"value": "a", "active": True}
    ];

    analysis = analyze_data(data_set, filters={"min_length": 1});
    print("\nData analysis:");
    print(f"  Unique values: {analysis['values']}");
    print(f"  Total: {analysis['total']}");
    print(f"  Metadata: {analysis['metadata']}");

    set_a = {1, 2, 3};
    set_b = {3, 4, 5};
    dict_a = {"x": 10, "y": 20};
    dict_b = {"y": 25, "z": 30};

    merged_set, merged_dict = merge_collections(set_a, set_b, dict_a, dict_b);
    print("\nMerged collections:");
    print(f"  Set: {merged_set}");
    print(f"  Dict: {merged_dict}");

    nested = {
        "users": {101, 102, 103},
        "config": {
            "settings": {"theme": "dark", "lang": "en"}
        },
        "tags": {"important", "reviewed"}
    };

    print("\nNested structure:", nested);
}