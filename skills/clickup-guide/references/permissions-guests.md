# Permissions & Guest Access

How to control what clients and team members can see in ClickUp.

## User Roles Overview

| Role | Capabilities | Limitations |
|------|--------------|-------------|
| **Owner** | Full control, billing, SSO config | Only one per Workspace |
| **Admin** | Manage users, settings, integrations | Cannot manage billing |
| **Member** | Create/edit content, use ClickApps | Cannot manage settings or users |
| **Guest** | View/edit shared items only | Cannot see Spaces, limited features |

## Permission Inheritance

Permissions flow down the hierarchy unless overridden:

```
Workspace (base permissions)
  ↓ inherits
Space (Space-level permissions)
  ↓ inherits (unless customized)
Folder → List → Task
```

**Override:** Set custom permissions at any level to break inheritance.

**Key principle:** More restrictive permissions at lower levels override inherited permissions.

## Guest Access for Clients

### Guest Types

| Type | Cost | Capabilities |
|------|------|--------------|
| **View Only Guest** | FREE | Can only view shared items |
| **Permission-Controlled Guest** | Paid (same as member) | Can edit, comment based on permissions |

**Business tier:** 5 free guests included, then $5/month each additional.

### What Guests CAN Do

- View tasks, Docs, and content in items shared with them
- Comment on shared items (if permission granted)
- Edit tasks (if permission granted)
- Upload attachments (if permission granted)
- Use basic views on shared items

### What Guests CANNOT Do

- See Spaces (guests are invited to Folders, Lists, or Tasks—never Spaces)
- Access items not explicitly shared with them
- Create new Spaces, Folders, or Lists
- See other Workspaces
- Use most ClickApps
- Create automations
- Access Dashboards (unless specifically shared)

### Inviting Guests

**Important:** Guests cannot be invited to Spaces—only to Folders, Lists, or Tasks.

**To invite a client:**
1. Navigate to the Folder, List, or Task to share
2. Click "Share" button
3. Enter client's email address
4. Select permission level:
   - **View** — See only, no changes
   - **Comment** — View + add comments
   - **Edit** — View + comment + modify tasks
   - **Full** — All permissions except admin
5. Click "Invite"

### Client Portal Methods

Three approaches for giving clients visibility:

**Method 1: Shared Folder (Recommended for most)**
- Invite client as Guest to their Folder
- They see all Lists within that Folder (except Private Lists)
- Simple, native, no extra setup

**Method 2: Public Doc Portal**
- Create Doc with embedded views
- Make Doc public (no login required)
- Client sees curated information without Guest account
- Good for limited visibility needs

**Method 3: Dashboard (Guest must be invited)**
- Build Dashboard with task widgets, charts, progress
- Share Dashboard with Guest
- Guest must have underlying task access for Task List widgets to work

## What to Hide from Clients

### Information to Keep Internal

| Category | Examples | How to Hide |
|----------|----------|-------------|
| Financials | Budget, profit margin, costs | Keep in Internal Notes List |
| Risk assessments | Project risk flags | Internal Notes or private Custom Fields |
| Team feedback | Performance notes, retrospectives | Internal Notes List |
| Other clients | References to other client work | Don't include in shared Lists |
| Strategy discussions | Internal debates, alternatives considered | Internal Notes List |
| Pricing/negotiation | Rate discussions, discount info | Internal Notes List |

### Hiding Custom Fields from Guests

1. Navigate to Custom Field Manager
2. Find the field to hide
3. Click Edit
4. Disable "Visible to guests and limited members"
5. Save

**⚠️ Important:** This setting applies to ALL guests, not individually selectable. If one client is a guest, and you hide a field, ALL client guests lose visibility to that field.

**⚠️ Important:** "Hide from Guest" does NOT apply to public link shares—only to Guest user access.

### The Internal Notes Pattern

For every client Folder, create an "Internal Notes" List:

```
FOLDER: Acme Corp
├── LIST: Active Engagement (shareable)
├── LIST: Deliverables (shareable)
└── LIST: Internal Notes (NEVER share)
```

**What goes in Internal Notes:**
- Risk assessments and flags
- Team discussions and decisions
- Budget tracking and margin analysis
- Competitor references (from other clients)
- Performance concerns
- Negotiation history

**Protection:** Never invite guests to this List. Keep it at default (inherited from Folder) but don't include in guest invitation.

## Private Spaces

For sensitive information entire teams shouldn't see:

### Creating a Private Space

1. Create new Space or edit existing
2. In Space settings, select "Private"
3. Add specific members who should have access

### Use Cases for Private Spaces

- **HR/People Ops** — Performance reviews, compensation, hiring
- **Finance** — Budgets, cash flow, sensitive projections
- **Executive** — Board materials, M&A, strategic planning
- **Specific Client** — If engagement requires extra confidentiality

**Caution:** Don't overuse Private Spaces. They fragment visibility and complicate reporting. Use sparingly for genuinely sensitive content.

## Common Permission Mistakes

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Inviting Guest to Space | Fails—guests can't access Spaces | Invite to Folder or List instead |
| Sharing Folder with internal notes | Client sees sensitive info | Create separate Internal Notes List, exclude from sharing |
| Public Dashboard | ClickUp doesn't support this | Use Guest access or scheduled email reports |
| Assuming hidden fields hide from public links | They don't | Use Guest access, not public links, for sensitive content |
| Giving client "Full" access | They can delete things | Use "Edit" or "Comment" instead |

## Permission Levels Explained

When sharing, these permission levels are available:

| Level | Can View | Can Comment | Can Edit Tasks | Can Delete | Can Manage Sharing |
|-------|----------|-------------|----------------|------------|-------------------|
| View | ✅ | ❌ | ❌ | ❌ | ❌ |
| Comment | ✅ | ✅ | ❌ | ❌ | ❌ |
| Edit | ✅ | ✅ | ✅ | ❌ | ❌ |
| Full | ✅ | ✅ | ✅ | ✅ | ✅ |

**Recommendation for clients:** "Comment" or "Edit" depending on whether they need to modify tasks or just provide feedback.

## Enterprise Security Controls

Enterprise tier adds critical controls for consulting firms:

| Control | What It Does |
|---------|--------------|
| Block public sharing | Prevent anyone from making Docs/views public |
| Restrict guest invitations | Control who can add external guests |
| Force private Spaces | New Spaces default to private |
| Audit logs | Track who did what, when |
| Private attachment links | Attachments require login to view |
| SSO enforcement | Microsoft, Okta, custom SAML |
| Data residency | Choose US, EU, or APAC data storage |

**When these matter:**
- Regulated industries (healthcare, finance)
- Clients with strict security requirements
- Need to demonstrate compliance in audits
- Preventing accidental data exposure

## Checklist: Setting Up Client Access

Before inviting a client as Guest:

- [ ] Client Folder exists with clear naming
- [ ] "Internal Notes" List created and NOT included in sharing
- [ ] Sensitive Custom Fields marked "Hide from Guests"
- [ ] Team knows which Lists are shared vs internal
- [ ] Permission level decided (View, Comment, or Edit)
- [ ] Test view as Guest to verify what they'll see
- [ ] Client briefed on how to access and use ClickUp
