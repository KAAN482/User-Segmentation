# Manuel Test Komutları

Bu komutları projenizi test etmek için kullanabilirsiniz. Kullandığınız terminale göre uygun olanı seçiniz.

## Yöntem 1: PowerShell (Önerilen)
Windows PowerShell kullanıyorsanız, `curl` yerine `Invoke-RestMethod` kullanmak en kolayıdır. Aşağıdaki blokları kopyalayıp terminale yapıştırın.

### 1. Basit Karşılaştırma (Sayısal)
Kullanıcı seviyesinin 10'dan büyük olup olmadığını test eder.

```powershell
$body = @{
    user = @{ level = 15 }
    segments = @{ is_high_level = "level > 10" }
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:3000/evaluate" -Method Post -Body $body -ContentType "application/json"
```

### 2. Büyük/Küçük Harf Duyarlılığı
SQL karşılaştırmaları standart olarak harf duyarlı olabilir.

```powershell
$body = @{
    user = @{ country = "Turkey" }
    segments = @{
        is_turkey = "country = 'Turkey'"
        is_turkey_lowercase = "country = 'turkey'"
    }
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:3000/evaluate" -Method Post -Body $body -ContentType "application/json"
```

### 3. Çoklu Koşullar (AND/OR)
Birden fazla koşulun test edilmesi.

```powershell
$body = @{
    user = @{ country = "Turkey"; purchase_amount = 12000 }
    segments = @{
        turkish_vip = "country = 'Turkey' AND purchase_amount >= 10000"
    }
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:3000/evaluate" -Method Post -Body $body -ContentType "application/json"
```

---

## Yöntem 2: Command Prompt (cmd.exe)
Eğer klasik Windows komut satırını (cmd) kullanıyorsanız `curl` kullanabilirsiniz. Ancak tırnak işaretlerini (`"`) kaçırmak için `\` kullanmak gerekir ve JSON tek satırda olmalıdır.

### 1. Basit Karşılaştırma
```cmd
curl -X POST http://localhost:3000/evaluate -H "Content-Type: application/json" -d "{\"user\": {\"level\": 15}, \"segments\": {\"is_high_level\": \"level > 10\"}}"
```

### 2. Büyük/Küçük Harf Duyarlılığı
```cmd
curl -X POST http://localhost:3000/evaluate -H "Content-Type: application/json" -d "{\"user\": {\"country\": \"Turkey\"}, \"segments\": {\"is_turkey\": \"country = 'Turkey'\", \"is_turkey_lowercase\": \"country = 'turkey'\"}}"
```

### 3. Çoklu Koşullar
```cmd
curl -X POST http://localhost:3000/evaluate -H "Content-Type: application/json" -d "{\"user\": {\"country\": \"Turkey\", \"purchase_amount\": 12000}, \"segments\": {\"turkish_vip\": \"country = 'Turkey' AND purchase_amount >= 10000\"}}"
```
