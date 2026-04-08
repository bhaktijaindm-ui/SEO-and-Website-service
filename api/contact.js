import { Resend } from 'resend';

// Your Private Resend API Key
const resend = new Resend('re_c27F6Fps_8uXEvLwEE83HcrgZ4Jm7MKVA');

export default async function handler(req, res) {
  // Ensure we only handle POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { name, email, website, service, message, website_url, plan } = req.body;

    // Normalizing data from different form types (Contact page vs Sidebar forms)
    const senderName = name || 'Interested Client';
    const senderEmail = email;
    const senderWebsite = website || website_url || 'N/A';
    const selectedService = service || 'General Inquiry';
    const selectedPlan = plan || 'Custom Selection';
    const senderMessage = message || 'Sent an inquiry via the sidebar audit form.';

    const { data, error } = await resend.emails.send({
      from: 'Portfolio Notifier <onboarding@resend.dev>', 
      to: ['bhaktijaindm@gmail.com'],
      subject: `New Lead: ${selectedService} (${selectedPlan})`,
      html: `
        <div style="font-family: sans-serif; max-width: 600px; line-height: 1.6;">
            <h2 style="color: #6366f1;">New Website Inquiry</h2>
            <hr style="border: 0; border-top: 1px solid #eee;">
            <p><strong>Name:</strong> ${senderName}</p>
            <p><strong>Email:</strong> ${senderEmail}</p>
            <p><strong>Website:</strong> ${senderWebsite}</p>
            <p><strong>Service:</strong> ${selectedService}</p>
            <p><strong>Package Interest:</strong> ${selectedPlan}</p>
            <div style="background: #f9f9f9; padding: 15px; border-radius: 8px; margin-top: 20px;">
                <strong>Message:</strong><br>
                ${senderMessage.replace(/\n/g, '<br>')}
            </div>
            <p style="font-size: 0.8rem; color: #888; margin-top: 30px;">This inquiry was sent from your professional portfolio dashboard.</p>
        </div>
      `,
    });

    if (error) {
      console.error('Resend Error:', error);
      // Fallback redirect even on mail error so user isn't stuck (logs will show the error)
      return res.redirect(303, '/thank-you?status=error');
    }

    // Success redirect
    return res.redirect(303, '/thank-you');

  } catch (err) {
    console.error('Server Internal Error:', err);
    return res.redirect(303, '/thank-you?status=server_error');
  }
}
