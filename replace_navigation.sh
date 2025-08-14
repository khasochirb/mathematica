#!/bin/bash

# Script to replace old navigation with new consistent navigation in all subject pages
echo "Starting navigation replacement for all subject pages..."

# Function to update a single file
update_file() {
    local file="$1"
    echo "Updating navigation in: $file"
    
    # Create a temporary file with the new navigation
    temp_file=$(mktemp)
    
    # Read the file and replace the old navigation section
    awk '
    BEGIN { in_header = 0; header_done = 0; }
    
    /<!-- Header -->/ { 
        in_header = 1; 
        print $0;
        next;
    }
    
    in_header && /<!-- Main -->/ { 
        in_header = 0; 
        header_done = 1;
        print $0;
        next;
    }
    
    in_header { 
        next; 
    }
    
    { print $0; }
    ' "$file" > "$temp_file"
    
    # Now insert the new navigation before the Main section
    awk '
    /<!-- Main -->/ {
        print "        <!-- Header -->";
        print "        <section id=\"header\">";
        print "            <div class=\"header-container\" style=\"display: flex; align-items: center; justify-content: space-between;\">";
        print "                <!-- Logo -->";
        print "                <div class=\"logo\">";
        print "                    <a href=\"../../index.html\"><img src=\"../../images/logo.png\" alt=\"International Math Hub Logo\" style=\"max-height: 60px;\"></a>";
        print "                </div>";
        print "";
        print "                <!-- Main Navigation -->";
        print "                <nav id=\"nav\">";
        print "                    <ul>";
        print "                        <li><a href=\"../../index.html\">Home</a></li>";
        print "                        ";
        print "                        <!-- Subjects Dropdown -->";
        print "                        <li class=\"has-dropdown\">";
        print "                            <a href=\"../../features.html\">Subjects</a>";
        print "                            <div class=\"dropdown subjects-dropdown\">";
        print "                                <div class=\"subjects-container\">";
        print "                                    <div class=\"subjects-grid\">";
        print "                                    <a href=\"../algebra/linear-and-quadratic-equations.html\" class=\"subject-item\">";
        print "                                        <i class=\"fas fa-calculator\"></i>";
        print "                                        <span>Algebra</span>";
        print "                                    </a>";
        print "                                    <a href=\"../geometry/euclidean-geometry.html\" class=\"subject-item\">";
        print "                                        <i class=\"fas fa-shapes\"></i>";
        print "                                        <span>Geometry</span>";
        print "                                    </a>";
        print "                                    <a href=\"../calculus/differentiation.html\" class=\"subject-item\">";
        print "                                        <i class=\"fas fa-chart-line\"></i>";
        print "                                        <span>Calculus</span>";
        print "                                    </a>";
        print "                                    <a href=\"../trigonometry/trigonometric-identities-and-formulas.html\" class=\"subject-item\">";
        print "                                        <i class=\"fas fa-wave-square\"></i>";
        print "                                        <span>Trigonometry</span>";
        print "                                    </a>";
        print "                                    <a href=\"../statistics/descriptive-statistics.html\" class=\"subject-item\">";
        print "                                        <i class=\"fas fa-chart-bar\"></i>";
        print "                                        <span>Statistics</span>";
        print "                                    </a>";
        print "                                    <a href=\"../complex-numbers/basic-operations.html\" class=\"subject-item\">";
        print "                                        <i class=\"fas fa-infinity\"></i>";
        print "                                        <span>Complex Numbers</span>";
        print "                                    </a>";
        print "                                    <a href=\"../matrices-and-determinants/matrix-operations.html\" class=\"subject-item\">";
        print "                                        <i class=\"fas fa-th\"></i>";
        print "                                        <span>Matrices</span>";
        print "                                    </a>";
        print "                                    <a href=\"../number-theory/divisibility-and-prime-numbers.html\" class=\"subject-item\">";
        print "                                        <i class=\"fas fa-hashtag\"></i>";
        print "                                        <span>Number Theory</span>";
        print "                                    </a>";
        print "                                    <a href=\"../probability/basic-probability-rules.html\" class=\"subject-item\">";
        print "                                        <i class=\"fas fa-dice\"></i>";
        print "                                        <span>Probability</span>";
        print "                                    </a>";
        print "                                    <a href=\"../sequences-and-series/arithmetic-and-geometric-sequences.html\" class=\"subject-item\">";
        print "                                        <i class=\"fas fa-list-ol\"></i>";
        print "                                        <span>Sequences & Series</span>";
        print "                                    </a>";
        print "                                    <a href=\"../graph-theory/graph-representation.html\" class=\"subject-item\">";
        print "                                        <i class=\"fas fa-project-diagram\"></i>";
        print "                                        <span>Graph Theory</span>";
        print "                                    </a>";
        print "                                    <a href=\"../combinatorics/counting-principles.html\" class=\"subject-item\">";
        print "                                        <i class=\"fas fa-cubes\"></i>";
        print "                                        <span>Combinatorics</span>";
        print "                                    </a>";
        print "                                    <a href=\"../inequalities/am-gm-inequality.html\" class=\"subject-item\">";
        print "                                        <i class=\"fas fa-not-equal\"></i>";
        print "                                        <span>Inequalities</span>";
        print "                                    </a>";
        print "                                    <a href=\"../logic-and-set-theory/basic-set-operations.html\" class=\"subject-item\">";
        print "                                        <i class=\"fas fa-circle-notch\"></i>";
        print "                                        <span>Logic & Set Theory</span>";
        print "                                    </a>";
        print "                                    <a href=\"../vectors-and-coordinate-geometry/vector-operations.html\" class=\"subject-item\">";
        print "                                        <i class=\"fas fa-arrows-alt\"></i>";
        print "                                        <span>Vectors</span>";
        print "                                    </a>";
        print "                                </div>";
        print "                            </div>";
        print "                        </li>";
        print "";
        print "                        <!-- Exam Prep Dropdown -->";
        print "                        <li class=\"has-dropdown\">";
        print "                            <a href=\"../../exam-prep.html\">Exam Prep</a>";
        print "                            <div class=\"dropdown\">";
        print "                                <div class=\"dropdown-grid\">";
        print "                                    <a href=\"../../quizz.html\" class=\"dropdown-item\">";
        print "                                        <i class=\"fas fa-clipboard-check\"></i>";
        print "                                        <span>Practice Tests</span>";
        print "                                    </a>";
        print "                                    <a href=\"../../exam-prep.html#solutions\" class=\"dropdown-item\">";
        print "                                        <i class=\"fas fa-lightbulb\"></i>";
        print "                                        <span>Test Solutions</span>";
        print "                                    </a>";
        print "                                    <a href=\"../../exam-prep.html#sat\" class=\"dropdown-item\">";
        print "                                        <i class=\"fas fa-graduation-cap\"></i>";
        print "                                        <span>SAT Math</span>";
        print "                                    </a>";
        print "                                    <a href=\"../../tutoring.html\" class=\"dropdown-item\">";
        print "                                        <i class=\"fas fa-user-graduate\"></i>";
        print "                                        <span>1-on-1 Tutoring</span>";
        print "                                    </a>";
        print "                                    <a href=\"../../exam-prep.html#olympiad\" class=\"dropdown-item\">";
        print "                                        <i class=\"fas fa-trophy\"></i>";
        print "                                        <span>Math Olympiad</span>";
        print "                                    </a>";
        print "                                    <a href=\"../../exam-prep.html#ap\" class=\"dropdown-item\">";
        print "                                        <i class=\"fas fa-medal\"></i>";
        print "                                        <span>AP Calculus</span>";
        print "                                    </a>";
        print "                                </div>";
        print "                            </li>";
        print "";
        print "                            <!-- Grades Dropdown -->";
        print "                            <li class=\"has-dropdown\">";
        print "                                <a href=\"../../grades.html\">Grades</a>";
        print "                                <div class=\"dropdown\">";
        print "                                    <div class=\"dropdown-grid\">";
        print "                                        <a href=\"../../grades.html#elementary\" class=\"dropdown-item\">";
        print "                                            <i class=\"fas fa-child\"></i>";
        print "                                            <span>Elementary School</span>";
        print "                                        </a>";
        print "                                        <a href=\"../../grades.html#middle\" class=\"dropdown-item\">";
        print "                                            <i class=\"fas fa-school\"></i>";
        print "                                            <span>Middle School</span>";
        print "                                        </a>";
        print "                                        <a href=\"../../grades.html#high\" class=\"dropdown-item\">";
        print "                                            <i class=\"fas fa-university\"></i>";
        print "                                            <span>High School</span>";
        print "                                        </a>";
        print "                                        <a href=\"../../grades.html#college\" class=\"dropdown-item\">";
        print "                                            <i class=\"fas fa-graduation-cap\"></i>";
        print "                                            <span>College</span>";
        print "                                        </a>";
        print "                                        <a href=\"../../grades.html#adult\" class=\"dropdown-item\">";
        print "                                            <i class=\"fas fa-user-tie\"></i>";
        print "                                            <span>Adult Learning</span>";
        print "                                        </a>";
        print "                                    </div>";
        print "                                </li>";
        print "";
        print "                                <!-- Company Dropdown -->";
        print "                                <li class=\"has-dropdown\">";
        print "                                    <a href=\"../../company.html\">Company</a>";
        print "                                    <div class=\"dropdown\">";
        print "                                        <div class=\"dropdown-grid\">";
        print "                                            <a href=\"../../company.html#about\" class=\"dropdown-item\">";
        print "                                                <i class=\"fas fa-info-circle\"></i>";
        print "                                                <span>About</span>";
        print "                                            </a>";
        print "                                            <a href=\"../../company.html#careers\" class=\"dropdown-item\">";
        print "                                                <i class=\"fas fa-briefcase\"></i>";
        print "                                                <span>Careers</span>";
        print "                                            </a>";
        print "                                            <a href=\"../../company.html#contact\" class=\"dropdown-item\">";
        print "                                                <i class=\"fas fa-envelope\"></i>";
        print "                                                <span>Contact</span>";
        print "                                            </a>";
        print "                                            <a href=\"../../company.html#team\" class=\"dropdown-item\">";
        print "                                                <i class=\"fas fa-users\"></i>";
        print "                                                <span>Our Team</span>";
        print "                                            </a>";
        print "                                        </div>";
        print "                                    </li>";
        print "";
        print "                                    <!-- Blog Button -->";
        print "                                    <li><a href=\"../../blog.html\">Blog</a></li>";
        print "                                </ul>";
        print "                            </nav>";
        print "";
        print "                            <!-- Call-to-Action Buttons -->";
        print "                            <div class=\"nav-cta-container\">";
        print "                                <a href=\"tel:+14153367764\" class=\"nav-phone\">";
        print "                                    <i class=\"fas fa-phone\"></i>";
        print "                                    +1 (415) 336-7764";
        print "                                </a>";
        print "                                <a href=\"../../tutoring.html\" class=\"nav-cta-btn\">Find Your Tutor</a>";
        print "                                <a href=\"../../contact.html\" class=\"nav-login\">Log In</a>";
        print "                            </div>";
        print "                        </div>";
        print "                    </section>";
        print "";
        print $0;
        next;
    }
    
    { print $0; }
    ' "$temp_file" > "$file"
    
    # Clean up temporary file
    rm "$temp_file"
}

# Find all HTML files in topics directory and update them
find topics -name "*.html" -type f | while read -r file; do
    update_file "$file"
done

echo "Navigation replacement completed for all subject pages!"

