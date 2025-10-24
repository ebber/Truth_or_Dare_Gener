# Truth or Dare Generator - Session State

**Last Updated:** 2025-10-24 13:40 PST
**Session Owner:** Erik
**AI Collaborator:** Claude Code (Sonnet 4.5)

---

## Project Overview

**Name:** Truth or Dare Generator
**Purpose:** A focused web component that generates random truth questions and dare challenges for group entertainment
**Use Case:** Shared kiosk-style app for in-person gatherings (parties, game nights). Users gather around a screen, click buttons, get prompts.

**Tech Stack:**
- Django 5.2.7 (Python 3.13)
- SQLite database (development)
- Single-page responsive web app
- No frontend framework (vanilla HTML/CSS/form handling)

---

## Foundational Principles

### 1. Secure, Scalable, Resilient Engineering
**"We build for eons to come"**
- Write code that's maintainable, extensible, and production-ready
- Consider security from day one, not as an afterthought
- Design for growth, even if current scope is narrow

### 2. Start Small, Evolve Iteratively
**"MVP as a seed, then grow it"**
- Begin with the smallest functional version
- Validate core concepts before adding complexity
- Each feature should build on a solid foundation

### 3. Security Creates Speed
**"Baking security into the bones enables fast, confident iteration"**
- Test-driven development (TDD) from the start
- Input validation and sanitization at every layer
- Secure defaults (CSRF protection, parameterized queries, etc.)
- Security hardening allows rapid feature development without fear

### 4. Scripts as SOPs
**"If a command runs 3+ times, script it"**
- Repetitive tasks become automated scripts
- Scripts serve as executable documentation
- Examples: running tests, seeding database, deploying, checking health

### 5. Meta-Thread: Continuous Improvement
**"Track adherence to best practices and learning"**
- Maintain awareness of software engineering ideals
- Document what we learn as we build
- Reflect on deviations and course-correct
- Code reviews (even self-reviews) before commits

---

## Current State

### Project Maturity: **Functional MVP** ✅

**What's Complete:**
- Core feature (random truth/dare generation) works perfectly
- Clean Django architecture with proper MVC separation
- 2 models: `TruthPrompt` and `DarePrompt` (with is_active flags, timestamps)
- 1 class-based view handling GET/POST requests
- 1 polished HTML template with modern CSS (purple gradients, glassmorphism)
- 20 truth questions seeded in database
- 20 dare challenges seeded in database
- 9 test cases covering models, views, and game logic
- Management command for data population (`populate_prompts`)
- Git repository initialized and transferred from old repo (GitHub auth issue resolved)

**What's In Progress:**
- Nothing actively being worked on (as of this session)

**What's Next (Immediate Priorities):**
1. **Admin Panel Registration** - Enable web-based content management
2. **UI Animations** - Polish the prompt reveal experience
3. **Content Expansion** - Add difficulty levels, categories, more prompts

### Security Status (Development Mode)

**Current Configuration:**
- ⚠️ DEBUG=True (expected for development)
- ⚠️ SECRET_KEY hardcoded in settings.py (needs environment variable)
- ⚠️ ALLOWED_HOSTS=[] (accepts any hostname)
- ✅ CSRF protection enabled
- ✅ SQLite for dev (appropriate, but Postgres needed for production)

**Before Production:**
- Move SECRET_KEY to environment variables
- Set DEBUG=False
- Configure ALLOWED_HOSTS to specific domains
- Migrate to PostgreSQL
- Add rate limiting for API endpoints

### Database State
- **Engine:** SQLite (db.sqlite3, 139KB)
- **Migrations:** Initial migration applied (2025-10-24 18:27:37)
- **Data:** 20 truths, 20 dares (all active)

### Tests
- **Coverage:** 9 test cases
- **Status:** All passing (last verified during codebase exploration)
- **Scope:** Models, views, game logic

---

## Tactical Position: Where We Are Now

### Last Activity (2025-10-24)
1. ✅ Transferred project from `truth-or-dare-app/` to `Truth_or_Dare_Gener/` (due to GitHub auth issues)
2. ✅ Kept all source code, database, virtual environment
3. ✅ Excluded old .git directory (new repo has fresh GitHub setup)
4. ✅ Analyzed codebase thoroughly
5. ✅ Created ROADMAP.md with phases and priorities
6. 🔄 **NOW:** Creating this session state file
7. ⏭️ **NEXT:** Push to remote repository

### Files Created This Session
- `ROADMAP.md` - Project roadmap with phases and priorities
- `.claude/session-state.md` - This file

### Files Modified This Session
- None yet (transfers only)

### Commands Run This Session
```bash
# Changed working directory
cd Truth_or_Dare_Gener

# Transferred files from old project
rsync -av --exclude='__pycache__' --exclude='*.pyc' --exclude='.git' truth-or-dare-app/ Truth_or_Dare_Gener/
```

---

## Architecture & Design Decisions

### Why Django?
- Batteries-included framework (admin, ORM, migrations, security)
- Perfect for rapid MVP development
- Well-suited for content-driven apps

### Why SQLite?
- Zero configuration for development
- Perfect for learning and prototyping
- Easy to version control and transfer
- **Note:** Will migrate to PostgreSQL for production

### Why No Frontend Framework?
- Current scope doesn't require React/Vue complexity
- Server-rendered templates are sufficient for simple interactions
- Can add JS animations without full framework
- **Future:** API endpoints will enable frontend framework integration if needed

### Why Class-Based Views?
- More extensible than function views
- Easier to add middleware and mixins later
- Django best practice for standard CRUD operations

---

## Key Learnings & Insights

### Session Insights
1. **Context Matters:** Initial assessment labeled missing features as "gaps," but with context (shared kiosk app), those features are intentionally out of scope
2. **Security First:** Even in MVP, flagging security issues (hardcoded secrets) early prevents technical debt
3. **Admin Panel Oversight:** Models not registered in admin is common oversight in tutorials, but critical for real apps
4. **Transfer Strategy:** Excluding .git but keeping venv saved significant setup time

### Development Patterns Observed
- **Bottom-Up:** Models → Views → Templates (classic Django flow)
- **Test-Driven Mindset:** Tests exist from early stage (good sign)
- **Minimalist:** No unnecessary dependencies or framework bloat
- **Pragmatic:** Inline CSS for MVP (can refactor later)

---

## Vibe & Working Style

### Collaboration Tone
- **Professional but Conversational:** Balance between technical rigor and approachability
- **Fact-Based Analysis:** Stick to observable reality, avoid speculation
- **Security-Conscious:** Always flag vulnerabilities, even in dev mode
- **Iterative:** Build small, test, expand

### Erik's Preferences (Observed)
- Appreciates detailed explanations with context
- Values security awareness
- Likes structured roadmaps and planning
- Prefers session state tracking for continuity

### Code Style
- PEP 8 compliant
- Django conventions followed
- Descriptive naming (no abbreviations)
- Separation of concerns

---

## Next Session: Quick Start Guide

When you return to this project in a future Claude Code session, follow these steps:

### 1. Read This File First
```bash
# Future Claude instance should run:
cat /Users/erik/Documents/projects/claude-code/Truth_or_Dare_Gener/.claude/session-state.md
```

### 2. Check Roadmap
```bash
cat /Users/erik/Documents/projects/claude-code/Truth_or_Dare_Gener/ROADMAP.md
```

### 3. Verify Environment
```bash
cd /Users/erik/Documents/projects/claude-code/Truth_or_Dare_Gener
source venv/bin/activate
python manage.py check  # Should show no issues
python manage.py test   # Should show 9 tests passing
```

### 4. Ask Erik
- "Where do you want to pick up?" or
- "Should we tackle [next priority from roadmap]?" or
- "Any new context since last session?"

---

## Scripts & SOPs

### Running Tests
```bash
# Standard test run
python manage.py test

# Verbose output
python manage.py test --verbosity=2

# Specific test
python manage.py test game.tests.GameViewTest
```

### Populating Database
```bash
# Clear and re-seed prompts
python manage.py populate_prompts
```

### Starting Development Server
```bash
# Activate virtual environment
source venv/bin/activate

# Run server
python manage.py runserver

# Access at: http://127.0.0.1:8000/
```

### Creating Admin User
```bash
python manage.py createsuperuser
# Follow prompts to set username, email, password
# Access admin at: http://127.0.0.1:8000/admin/
```

### Git Operations
```bash
# Check status
git status

# Stage changes
git add .

# Commit with descriptive message
git commit -m "Descriptive message of changes"

# Push to remote
git push origin main
```

### Dependency Management
```bash
# Install dependencies
pip install -r requirements.txt

# Update requirements after adding new package
pip freeze > requirements.txt
```

---

## Meta-Thread: Adherence to Best Practices

### What We're Doing Well ✅
- **Tests exist from the start** (Principle 3: Security Creates Speed)
- **Management command for seeding** (Principle 4: Scripts as SOPs)
- **Clean architecture** (Principle 1: Build for eons)
- **Iterative approach** (Principle 2: Start small, evolve)
- **Security flagged early** (Principle 3: Bake security into bones)

### Where We Can Improve 🔄
- **Docstrings:** Add comprehensive docstrings to all functions/classes
- **Environment Variables:** Move SECRET_KEY out of settings.py
- **Admin Registration:** Models should be in admin panel for content management
- **Test Coverage:** Expand to 95%+ coverage
- **API Documentation:** When API is added, document with OpenAPI/Swagger

### Lessons Learned 📚
1. **Always transfer venv when possible** - Saves pip install time, ensures exact versions
2. **Exclude .git on transfers** - Prevents bringing over auth issues
3. **Security audit even in dev** - Easier to fix early than retrofit later
4. **Context changes assessment** - What looks like "missing features" might be intentional scope

---

## Open Questions & Blockers

### Questions for Erik
- None currently

### Technical Blockers
- None

### Decisions Needed
- None at this moment (roadmap is clear)

---

## Future Session TODOs

### Immediate (Next Session)
1. Register models in admin panel
2. Create superuser for admin access
3. Add basic animations to prompt reveal

### Short-Term (Next 2-3 Sessions)
1. Add difficulty levels to prompts
2. Expand database to 50+ truths and dares
3. Create REST API endpoints

### Long-Term (Before Production)
1. Security hardening (environment variables, ALLOWED_HOSTS)
2. Migrate to PostgreSQL
3. Add rate limiting
4. Deployment configuration

---

**End of Session State**

*This file will be updated at natural breakpoints, at the end of sessions, and when explicitly requested by Erik.*
