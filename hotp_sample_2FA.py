import hmac
import hashlib
import struct
import base64


def hotp(secret, counter, digits=6):

    """
    Generate an HOTP value using a shared secret and counter.

    :param secret: The shared secret (in base32 encoding).
    :param counter: The counter value.
    :param digits: The number of digits for the OTP (default is 6).
    :return: The HOTP value as a string.
    """
    # Decode the base32 secret to bytes
    key = base64.b32decode(secret, True)
    print(f"value of secret key {key}")
    # Pack the counter as an 8-byte integer (big-endian)
    counter_bytes = struct.pack(">Q", counter)
    print(f"value of counter byte {counter_bytes}")

    # Generate the HMAC-SHA1 hash
    hmac_hash = hmac.new(key, counter_bytes, hashlib.sha1).digest()
    print(f"value of hmac_hash {hmac_hash}")

    # Extract a 4-byte dynamic binary code from the HMAC
    offset = hmac_hash[-1] & 0x0F
    print(f"value of offset key {offset}")

    code = (struct.unpack(">I", hmac_hash[offset:offset + 4])[0] & 0x7FFFFFFF) % (10 ** digits)
    print(f"value of code key {code}")

    # Return the HOTP value as a zero-padded string
    return str(code).zfill(digits)


# Example usage
if __name__ == "__main__":
    # Shared secret in base32 (can be any base32 string)
    secret = "JBSWY3DPEHPK3PXP"  # Example base32 secret

    # Example counter value
    counter = 4

    # Generate HOTP
    otp = hotp(secret, counter)
    print(f"HOTP for counter {counter}: {otp}")
