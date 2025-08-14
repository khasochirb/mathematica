#!/bin/bash

# Script to update all subject pages with consistent navigation
echo "Starting navigation update for all subject pages..."

# Function to update a single file
update_file() {
    local file="$1"
    echo "Updating: $file"
    
    # Add required CSS files if they don't exist
    if ! grep -q "dropdown-nav.css" "$file"; then
        sed -i '' 's|<link rel="stylesheet" href="../../assets/css/topic-pages.css" />|<link rel="stylesheet" href="../../assets/css/topic-pages.css" />\n    <link rel="stylesheet" href="../../assets/css/dropdown-nav.css" />\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" />|' "$file"
    fi
    
    # Add dropdown JavaScript if it doesn't exist
    if ! grep -q "Dropdown Navigation Script" "$file"; then
        sed -i '' 's|</body>|    <!-- Dropdown Navigation Script -->\n    <script>\n        document.addEventListener("DOMContentLoaded", function() {\n            // Handle dropdown navigation\n            const dropdowns = document.querySelectorAll(".has-dropdown");\n            \n            dropdowns.forEach(dropdown => {\n                const link = dropdown.querySelector("a");\n                const dropdownMenu = dropdown.querySelector(".dropdown");\n                \n                // Show dropdown on hover\n                dropdown.addEventListener("mouseenter", function() {\n                    dropdownMenu.style.display = "block";\n                });\n                \n                // Hide dropdown when mouse leaves\n                dropdown.addEventListener("mouseleave", function() {\n                    dropdownMenu.style.display = "none";\n                });\n                \n                // Also handle click for mobile\n                link.addEventListener("click", function(e) {\n                    if (window.innerWidth <= 768) {\n                        e.preventDefault();\n                        dropdownMenu.style.display = dropdownMenu.style.display === "block" ? "none" : "block";\n                    }\n                });\n            });\n            \n            // Close dropdowns when clicking outside\n            document.addEventListener("click", function(e) {\n                if (!e.target.closest(".has-dropdown")) {\n                    document.querySelectorAll(".dropdown").forEach(dropdown => {\n                        dropdown.style.display = "none";\n                    });\n                }\n            });\n        });\n    </script>\n</body>|' "$file"
    fi
}

# Find all HTML files in topics directory and update them
find topics -name "*.html" -type f | while read -r file; do
    update_file "$file"
done

echo "Navigation update completed for all subject pages!"

