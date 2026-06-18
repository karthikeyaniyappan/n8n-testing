## Trimble Identity (TID)

- **Trimble ID** is a centralized authentication service built on industry-standard protocols: **OAuth 2.0**, **OpenID Connect**, and **SAML 2.0**.
- It also handles **app-to-app** authentication via **client credentials**.
- Supports **MFA** (Multi-Factor Authentication).

---

## OAuth 2.0, OpenID Connect & SAML 2.0

| Protocol | Purpose | Question it answers | Output |
|----------|---------|---------------------|--------|
| **OAuth 2.0** | Authorization (access) | Can this app access my data? | Access token |
| **OpenID Connect** | Authentication (identity) | Who is the user? | ID token + access token (JSON) |
| **SAML 2.0** | Authentication (SSO) | Who is the user? (via company login) | SAML assertion (XML) |

- OpenID Connect user details come from the **IDP (Identity Provider)** — e.g. Trimble Identity at `id.trimble.com`.

---

## IAM (Identity and Access Management)

- IAM answers two questions:
  1. **Who are you?** (Identity)
  2. **What are you allowed to do?** (Access)

**How it works (user login flow):**

1. User opens a Trimble app and clicks **Sign in**
2. App redirects to **IAM**
3. IAM verifies identity
4. IAM returns **tokens** (who you are + what you can access)

> **TID is inside IAM** — Trimble Identity is the authentication component within the broader IAM platform.

---

## API Endpoints

Base host: `https://id.trimble.com`

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/oauth/authorize` | GET | Start login / authorization |
| `/oauth/token` | POST | Exchange code for tokens / refresh tokens |
| `/oauth/userinfo` | GET | Get user profile details |
| `/oauth/logout` | GET | Log user out |
| `/oauth/revoke` | POST | Revoke/invalidate a refresh token |

### Authorize — `GET /oauth/authorize`

- Supports three **response_types**: `code`, `id_token`, `token`
- If **`code`** is present in parameters, **JWTs are not needed for authorization**
- If **`code`** is present, call **`POST /oauth/token`** to exchange the code for an access token (and ID token / refresh token)

---

## Authorization Code with PKCE

**PKCE** = Proof Key for Code Exchange

- Does **not require `client_secret`** in the `/token` request
- Mobile and browser apps **cannot safely store client secret** — PKCE is designed for these apps

**How it works:**

1. App **generates** `code_verifier`, `code_challenge`, and `code_challenge_method` (`S256`) **before** calling `/oauth/authorize`
2. Send `code_challenge` + `code_challenge_method` in the **authorize** request
3. User logs in → redirect back with **authorization code**
4. Call **`POST /oauth/token`** with the **code** + **`code_verifier`** to get access token (and ID token / refresh token)

> **Trimble-specific:** Uses **Serial PKCE** — a new (`code_verifier`, `code_challenge`) pair is required on **each token and refresh request**.
