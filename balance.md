# Game Balance Plan

This document outlines the proposed game balance adjustments for both Mini-Boss and Ultimate Boss fights, aiming for a more consistent, challenging, and engaging player experience.

---

## 1. Player Class Damage & HP Overview (Current)

*   **Summoner**: 220-280 damage per turn (Average: 250) | HP: 400
*   **Shadowblade**: 120-160 damage per turn (Average: 140) - Attacks twice in mini-boss, more frequent in ultimate. | HP: 500
*   **Scholar**: 150-180 damage per turn (Average: 165) | HP: 450
*   **Guardian**: 110-190 damage per turn (Average: 150) | HP: 650 (Proposed: 800)

---

## 2. Mini-Boss Fight Balance Plan

Designed for a consistent and challenging solo experience, aiming for fights lasting approximately 4-5 rounds.

*   **Boss HP**: **1200 HP**
    *   Provides a balanced fight duration against any of the solo classes.
*   **Boss Damage**: **110 - 140** per attack.
    *   This range makes the fight a real threat without being unfair.

---

## 3. Ultimate Boss Fight Balance Plan

Designed for an epic 4-player party encounter that feels strategic and allows each class to contribute meaningfully.

*   **Boss HP**: **6500 HP**
    *   Built to withstand about 3-4 full attack cycles from the party, requiring substantial effort and coordination.

*   **Boss AoE Damage (per player, per hit)**:
    *   Damage is tailored to each class's role, emphasizing the Guardian's tankiness and requiring strategic health management.
    *   **Guardian**: 100 - 150
    *   **Scholar**: 40 - 80
    *   **Shadowblade & Summoner**: 60 - 120

*   **Player HP Adjustment**:
    *   **Guardian**: Increase HP from 650 to **800**.
        *   This provides the Guardian with increased survivability, allowing them to withstand one additional hit in both mini-boss and ultimate boss scenarios, reinforcing their tank role.

*   **Turn Order (14-Turn Cycle)**:
    *   This revised turn order ensures the Shadowblade feels fast and powerful, while making the Guardian's role more active and engaging.
    *   **Turn Sequence**:
        ```
        [
            "boss", "player_1", "player_2", "player_4", "player_1", "player_3",
            "boss", "player_3", "player_2", "player_1", "player_4", "player_1", "player_2", "player_1"
        ]
        ```
    *   **Turns per Player in Cycle**:
        *   **Shadowblade**: 5
        *   **Scholar**: 3
        *   **Guardian**: 2
        *   **Summoner**: 2
