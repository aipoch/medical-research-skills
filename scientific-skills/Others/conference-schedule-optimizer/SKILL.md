---
name: conference-schedule-optimizer
description: Use when planning conference schedules, optimizing session selection at scientific meetings, managing time between presentations, or maximizing networking at academic conferences. Creates personalized schedules balancing learning, networking, and career development for medical and scientific conferences.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Conference Schedule Optimizer

Create optimal conference schedules balancing learning, networking, and career development for scientific and medical conferences.

## Quick Start

```python
from scripts.schedule_optimizer import ConferenceScheduler

scheduler = ConferenceScheduler()

# Generate optimized schedule
schedule = scheduler.optimize(
    conference="ASHG2024",
    interests=["genomics", "bioinformatics", "rare diseases"],
    constraints={"avoid_mornings": True, "networking_priority": "high"}
)

# Export to calendar
scheduler.export(schedule, format="ical", filename="my_conference.ics")
```

## Core Capabilities

### 1. Session Prioritization

```python
priorities = scheduler.prioritize_sessions(
    sessions=conference_sessions,
    criteria={
        "topic_relevance": 0.35,
        "speaker_reputation": 0.25,
        "career_value": 0.20,
        "networking_opportunity": 0.20
    }
)
```

**Prioritization Matrix:**

| Factor | Weight | How Measured |
|--------|--------|--------------|
| Topic Relevance | 35% | Keyword matching with your research |
| Speaker Impact | 25% | Citation count, h-index, previous talks |
| Career Value | 20% | Job opportunities, collaborations |
| Networking | 20% | Attendee overlap, social events |

### 2. Schedule Optimization

```python
optimized_schedule = scheduler.create_schedule(
    sessions=priorities,
    constraints={
        "max_consecutive_sessions": 3,
        "lunch_break": "12:00-13:00",
        "must_attend": ["Keynote: Dr. Smith", "Workshop: CRISPR"],
        "avoid": ["conflict_of_interest_sessions"]
    }
)
```

### 3. Conflict Resolution

```python
resolved = scheduler.resolve_conflicts(
    overlapping_sessions=[session_a, session_b],
    strategy="attend_record_delegate"
)
```

**Conflict Resolution Strategies:**

| Strategy | Best For | Implementation |
|----------|----------|----------------|
| Attend + Record | High-priority talk | Attend live, watch recording later |
| Split Time | Equal priority | 20 min each, network after |
| Delegate | Team attending | Colleague attends, shares notes |
| Poster Alternative | Overlapping talks | Visit presenter's poster session |

### 4. Networking Planner

```python
networking_blocks = scheduler.plan_networking(
    target_attendees=[
        {"name": "Dr. Smith", "institution": "Stanford", "topic": "Genomics"},
        {"name": "Prof. Johnson", "institution": "Broad", "topic": "CRISPR"}
    ],
    strategy="coffee_chats",
    buffer_minutes=15
)
```

**Networking Tactics:**
- **Coffee Chats**: Schedule 15-min meetings before/after sessions
- **Poster Sessions**: High-quality conversations in relaxed setting
- **Social Events**: Evening receptions for informal networking
- **Twitter/X**: Live-tweet to connect with remote attendees

### 5. Travel Time Calculator

```python
schedule_with_travel = scheduler.add_travel_time(
    base_schedule,
    venue_map="conference_center.pdf",
    walking_speed="normal",  # or "slow" with poster tubes
    buffer_percent=20
)
```

## CLI Usage

```bash
# Optimize from conference program PDF
python scripts/schedule_optimizer.py \
  --program ashg2024_program.pdf \
  --interests "genomics,bioinformatics,ethics" \
  --constraints "no_mornings,prefer_posters" \
  --output my_schedule.ics

# Real-time update with room changes
python scripts/schedule_optimizer.py \
  --conference ASHG2024 \
  --update --notify

# Generate networking targets
python scripts/schedule_optimizer.py \
  --conference ASHG2024 \
  --mode networking \
  --my-research "rare disease genomics" \
  --output targets.csv
```

## Common Patterns

### Pattern 1: First-Time Attendee

**Goal**: Maximize learning, minimize overwhelm

```python
schedule = scheduler.optimize(
    conference="ISMRM2024",
    experience_level="first_time",
    strategy="breadth_over_depth",
    include_tutorials=True,
    social_events_priority="high"
)
```

### Pattern 2: Job Seeker

**Goal**: Network with target institutions

```python
schedule = scheduler.optimize(
    conference="SFN2024",
    goals=["job_search", "networking"],
    target_institutions=["NIH", "Stanford", "Genentech"],
    career_sessions_priority="must_attend"
)
```

### Pattern 3: Poster Presenter

**Goal**: Balance presenting with attending

```python
schedule = scheduler.optimize(
    conference="AGU2024",
    my_poster_session="Tuesday 2-4pm",
    conflicts_strategy="skip_lower_priority",
    networking_during_poster=True
)
```

## Quality Checklist

**Pre-Conference (2 weeks before):**
- [ ] Download conference app/program
- [ ] Flag 3 "must-attend" sessions per day
- [ ] Identify 5-10 people to meet
- [ ] Schedule non-conference meetings outside conference hours
- [ ] Download and review key papers from speakers

**During Conference:**
- [ ] Check schedule each morning for updates
- [ ] Take notes in unified location (app or notebook)
- [ ] Block 30-min daily for exhibit hall
- [ ] Stay hydrated and take walking breaks
- [ ] Tweet key insights (tag speakers, use conference hashtag)

**Post-Conference (within 48 hours):**
- [ ] Email new contacts with specific follow-up
- [ ] Organize notes by actionable items
- [ ] Share key learnings with lab/team
- [ ] Update CV with conference activities

## Common Pitfalls

❌ **Over-scheduling**: No breaks between sessions
✅ **Buffer time**: 15-min gaps for transitions and networking

❌ **Session hopping**: Leaving talks early
✅ **Commit fully**: Attend entire session or don't go

❌ **Skipping meals**: Running from session to session
✅ **Scheduled breaks**: Block lunch, rest, and processing time

---

**Skill ID**: 206 | **Version**: 1.0 | **License**: MIT
