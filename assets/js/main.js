function openPortfolioModal(url) {
  const portfolioModal = new bootstrap.Modal('#modalPortfolio', {
    keyboard:false
  });
  const portfolioPreview = document.getElementById("portfolioPreview");
  portfolioPreview.setAttribute("src", url);
  portfolioModal.show();
}
