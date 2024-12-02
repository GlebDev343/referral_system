
# Referral System API

This project implements a referral system using Django, DRF, and PostgreSQL. It allows users to authenticate via phone number, manage referral codes, and track referrals.

## Features

1. Phone number authentication with OTP.
2. Randomly generated 6-character referral codes.
3. Activation of referral codes.
4. View profile with referral details.
5. Track users referred by a given user.

## API Endpoints

### 1. Authentication

#### Request OTP
- **Endpoint**: `/api/users/register/`
- **Method**: `POST`
- **Payload**:
```json
{
  "phone_number": "+1234567890"
}
```
- **Response**:
```json
{
  "message": "Verification code sent."
}
```

#### Verify OTP
- **Endpoint**: `/api/users/verify/`
- **Method**: `POST`
- **Payload**:
```json
{
  "phone_number": "+1234567890",
  "verification_code": "1234"
}
```
- **Response**:
```json
{
    "message": "User authenticated",
    "new_user": "True",
    "token": "JWT_AUTH_TOKEN"
 
}
```

### 2. User Profile

#### Get Profile
- **Endpoint**: `/api/users/profile/`
- **Method**: `GET`
- **Headers**:
```json
{
  "Authorization": "Bearer <JWT_AUTH_TOKEN>"
}
```
- **Response**:
```json
{
  "phone_number": "+1234567890",
  "invite_code": "ABC123",
  "activated_invite_code": "XYZ789",
  "referred_users": ["+9876543210", "+6549873210"]
}
```

#### Activate Referral Code
- **Endpoint**: `/api/users/profile/`
- **Method**: `POST`
- **Headers**:
```json
{
  "Authorization": "Bearer <JWT_AUTH_TOKEN>"
}
```
- **Payload**:
```json
{
  "invite_code": "XYZ789"
}
```
- **Response**:
```json
{
  "message": "Invite code applied."
}
```
## Documentation

- Postman collection is available for testing API.
