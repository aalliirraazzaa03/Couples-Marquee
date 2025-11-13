from django.db import models

# ---------- Vendor Table ----------
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    vendor_of = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.vendor_of})"


# ---------- Payment Table ----------
class Payment(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_for = models.CharField(max_length=100)
    via = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment to {self.vendor.name} - {self.amount}"


# ---------- Expense Table ----------
class Expense(models.Model):
    date = models.DateField()
    purpose = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_asset = models.BooleanField(default=False)  # checkbox in frontend
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.purpose} - {self.amount}"
