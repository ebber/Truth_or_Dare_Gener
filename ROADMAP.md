# Truth or Dare Generator - Project Roadmap

## Project Vision
A focused web component that generates random truth questions and dare challenges for group entertainment. Users gather around a shared screen, click buttons, and receive prompts for their game.

---

## Current Status: **Functional MVP** ✅

### Completed Features
- [x] Core truth/dare random generation
- [x] Django project setup (5.2.7)
- [x] Database models with timestamps and active flags
- [x] Responsive web UI with modern glassmorphism design
- [x] CSRF-protected form submissions
- [x] Database seeding command (`populate_prompts`)
- [x] Test suite (9 test cases covering models, views, logic)
- [x] 20 truth questions in database
- [x] 20 dare challenges in database
- [x] Git repository initialized with proper .gitignore

---

## Roadmap

### Phase 1: Content Management & Polish (Next Up)
**Priority: HIGH**

- [ ] **Admin Panel Registration**
  - Register TruthPrompt and DarePrompt models in admin
  - Add list display, filters, and search
  - Create superuser for content management
  - Document admin access in README

- [ ] **UI Enhancements**
  - Add animations on prompt reveal (fade-in, slide effects)
  - Add loading states on button clicks
  - Add sound effects (optional, with mute toggle)
  - Improve mobile responsiveness testing

- [ ] **Content Expansion**
  - Add difficulty levels (mild, medium, spicy) to prompts
  - Expand database to 50+ truths and 50+ dares
  - Add category tags (funny, embarrassing, physical, creative)

### Phase 2: API & Integrations
**Priority: MEDIUM**

- [ ] **REST API Endpoints**
  - `GET /api/truth/` - Returns random truth
  - `GET /api/dare/` - Returns random dare
  - `GET /api/random/` - Returns random prompt (either type)
  - JSON responses for third-party integrations

- [ ] **Advanced Filtering**
  - Filter by difficulty level
  - Filter by category
  - Query parameters for API customization

### Phase 3: Production Readiness
**Priority: MEDIUM (before public deployment)**

- [ ] **Security Hardening**
  - Move SECRET_KEY to environment variables
  - Set DEBUG=False for production
  - Configure ALLOWED_HOSTS properly
  - Add rate limiting for API endpoints
  - Security audit and penetration testing

- [ ] **Performance & Scalability**
  - Migrate from SQLite to PostgreSQL
  - Add database query optimization
  - Implement caching for frequently accessed prompts
  - Load testing and performance benchmarks

- [ ] **Deployment**
  - Dockerize application
  - CI/CD pipeline setup
  - Production deployment guide
  - Health check endpoints

### Phase 4: Future Enhancements (Nice-to-Have)
**Priority: LOW**

- [ ] Multiple language support (i18n)
- [ ] Theme customization (color schemes, fonts)
- [ ] Print/share functionality for prompts
- [ ] Analytics dashboard (most popular prompts)
- [ ] Custom prompt submission form (crowd-sourced content)
- [ ] Voice assistant integration (Alexa, Google Home)
- [ ] Progressive Web App (PWA) for offline use

---

## Out of Scope (By Design)
These features are **intentionally excluded** to maintain focus:

- ❌ User authentication/profiles
- ❌ Game state tracking (rounds, scoring)
- ❌ Multiplayer/session management
- ❌ Player history or saved games
- ❌ Social media integration
- ❌ Leaderboards

**Reasoning:** This is a shared kiosk-style component for in-person gatherings, not a personal gaming platform.

---

## Technical Debt & Maintenance
- [ ] Add docstrings to all views and functions
- [ ] Expand test coverage to 95%+
- [ ] Add integration tests for full request/response cycle
- [ ] Create API documentation (OpenAPI/Swagger)
- [ ] Add logging for debugging and monitoring
- [ ] Dependency updates (automated with Dependabot)

---

## Metrics for Success
- **Phase 1 Complete:** Admin can easily manage content, UI feels polished
- **Phase 2 Complete:** External apps can integrate via stable API
- **Phase 3 Complete:** App runs securely and reliably in production
- **Phase 4 Complete:** App supports diverse use cases and audiences

---

**Last Updated:** 2025-10-24
**Maintained By:** Erik (with Claude Code assistance)
