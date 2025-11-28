# Multi-stage build for minimal image size
FROM python:3.11-alpine AS builder

# Install Flask in a temporary location
RUN pip install --no-cache-dir --target=/install flask

# Final stage - minimal runtime
FROM python:3.11-alpine

# Create non-root user
RUN addgroup -g 1000 appuser && \
    adduser -D -u 1000 -G appuser appuser

# Set working directory
WORKDIR /app

# Copy only necessary Python packages from builder
COPY --from=builder /install /usr/local/lib/python3.11/site-packages/

# Copy application files with proper ownership
COPY --chown=appuser:appuser app.py wordlist.txt ./

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 4001

# Run application
CMD ["python", "app.py"]
