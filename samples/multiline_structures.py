def create_user_profile(name, age, email) {
    profile = {
      "personal": {
        "name": name,
        "age": age,
        "email": email
      },
      "preferences": {
        "theme": "dark",
        "notifications": True
      },
      "metadata": {
        "created": "2024-01-01",
        "updated": "2024-01-15"
      }
    };

    return profile;
}

def process_config() {
    config = {
      "database": {
        "host": "localhost",
        "port": 5432,
        "credentials": {
          "username": "admin",
          "password": "secret"
        }
      },
      "api": {
        "endpoints": ["/users", "/posts", "/comments"],
        "rate_limit": 1000
      }
    };

    return config;
}

def analyze_tags() {
    tags = {
      "python",
      "golang",
      "rust",
      "javascript"
    };

    categories = {
      "languages": {
        "compiled": {"rust", "golang"},
        "interpreted": {"python", "javascript"}
      },
      "frameworks": {
        "web": {"django", "flask", "gin"},
        "data": {"pandas", "numpy"}
      }
    };

    return tags, categories;
}

if __name__ == "__main__" {
    user = create_user_profile("Alice", 30, "alice@example.com");
    print("User Profile:");
    print(f"  Name: {user['personal']['name']}");
    print(f"  Age: {user['personal']['age']}");
    print(f"  Theme: {user['preferences']['theme']}");

    print("\nConfig:");
    cfg = process_config();
    print(f"  DB Host: {cfg['database']['host']}");
    print(f"  DB Port: {cfg['database']['port']}");
    print(f"  API Endpoints: {cfg['api']['endpoints']}");

    print("\nTags Analysis:");
    tags, categories = analyze_tags();
    print(f"  All tags: {tags}");
    print(f"  Compiled languages: {categories['languages']['compiled']}");
    print(f"  Web frameworks: {categories['frameworks']['web']}");
}