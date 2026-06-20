/*
 * Compile: g++ -std=c++17 -o ex5 ex5.cpp
 */
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

int main() {
    std::map<std::string, std::vector<int>> gradebook = {
        {"alice",   {90, 85, 92}},
        {"bob",     {78, 88}},
        {"charlie", {95, 70, 80}},
    };

    std::map<std::string, int> averages;
    for (auto& [name, scores] : gradebook) {
        int sum = 0;
        for (int s : scores) sum += s;
        averages[name] = sum / scores.size();
    }

    // FIX: std::map iterators are not random-access, and its elements are pairs of const Key and Value.
    // std::sort requires random-access iterators and mutable elements.
    // Solution: copy to a vector and sort the vector.
    std::vector<std::pair<std::string, int>> sorted_averages(averages.begin(), averages.end());
    std::sort(sorted_averages.begin(), sorted_averages.end(), 
        [](const auto& a, const auto& b) {
            return a.second > b.second; // Sort descending by score
        });

    std::cout << "Rankings:" << std::endl;
    for (auto& [name, avg] : sorted_averages) {
        std::cout << "  " << name << ": " << avg << std::endl;
    }

    return 0;
}
